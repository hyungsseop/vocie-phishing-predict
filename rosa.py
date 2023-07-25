import os
import librosa
import soundfile as sf
import subprocess

def get_length(input_video):
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', input_video], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return float(result.stdout)

def trim_audio_data(audio_file, save_file):

    video_time = get_length(audio_file)

    sr = 16000
    sec = 20
    
    y, sr = librosa.load(audio_file, sr=sr)
    for i in range(int(video_time/20)+1):

        ny = y[sr*i*sec:sr*(i+1)*sec]

        sf.write(save_file + f'_{i}.wav', ny, sr)


file_list = os.listdir(os.getcwd()+'\original_data')
path = os.getcwd()+'\original_data'
new_path = os.getcwd()+'\preprocessing_data'


idx = 0
for file in file_list:
    print(file)
    print(librosa.__version__)
    trim_audio_data(path+"\\"+file, new_path+"\\"+f"{idx}")