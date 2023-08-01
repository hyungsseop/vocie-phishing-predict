import os
import librosa
import soundfile as sf
import subprocess
import numpy as np
import torchaudio

def get_length(input_video):
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', input_video], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return float(result.stdout)

def wav_trim_audio_data(audio_file, save_file,start, end):

    sr = 16000
    
    y, sr = librosa.load(audio_file, sr=sr)

    ny = y[:sr*int(end)]

    sf.write(save_file + '.wav', ny, sr)

def split_trim_audio_data(audio_file, save_file,time_stamp):

    video_time = get_length(audio_file)

    sr = 16000
    
    y, sr = librosa.load(audio_file, sr=sr)
    for i in range(len(time_stamp)-1):

        ny = y[sr*time_stamp[i]:sr*time_stamp[i+1]]

        sf.write(save_file + f'_{i}.wav', ny, sr)

def pyannote(file):
    torchaudio.set_audio_backend("soundfile")

    time_list = []

    from pyannote.audio import Pipeline
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1",
                                        use_auth_token="")

    diarization = pipeline(file, num_speakers=2)

    for turn, _, speaker in diarization.itertracks(yield_label=True):
        print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")
        #time_list[0].append(np.floor(turn.start))
        time_list.append(np.ceil(turn.end))
        #time_list[2].append(speaker)
        # start=0.2s stop=1.5s speaker_0

    return time_list


def main():
    #day = input("데이터를 처리할 날짜를 입력해주세요 : ex)0717")
    day = "0727"
    data_path = f"data/{day}"
    original_path = data_path + "/original"

    file_list = os.listdir(original_path)
    print(f"{day} 데이터에 대해 전처리를 시작합니다.")
    print(f"작업 파일 대상 갯수 : {len(file_list)}")

    wav_path = data_path+'/wav'
    idx = 0
    for file in file_list:
        audio_time = get_length(original_path+"\\"+file)
        wav_trim_audio_data(original_path+"/"+file, wav_path+"/"+f"{idx}",0,audio_time)
        idx += 1


    wav_path = data_path + "/wav"

    file_list = os.listdir(wav_path)

    split_path = data_path+'/split'
    idx2 = 0
    for file in file_list:
        audio_time = get_length(wav_path+"/"+file)

        end = pyannote(wav_path+"/"+file)

        time_stamp = []
        time_stamp.append(0)
        for i in range(len(end)-1):
            if end[i+1] - end[i] > 20:
                tmp = int(np.ceil(end[i+1] - end[i])/19)
                for j in range(tmp):
                    time_stamp.append(time_stamp[-1]+19)
            elif int(end[i]) - time_stamp[-1] >20:
                time_stamp.append(int(end[i-1])) 
        time_stamp.append(int(end[-1]))

        split_trim_audio_data(wav_path+"/"+file, split_path+"/"+f"{idx2}",time_stamp)
        idx2 += 1 


main()