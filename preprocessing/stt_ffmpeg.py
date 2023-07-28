import ffmpeg
import subprocess
import os

def get_length(input_video):
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', input_video], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return float(result.stdout)

def file_preprocessing():
    file_list = os.listdir(os.getcwd()+'\original_data')
    path = os.getcwd()+'\original_data'

    idx = 1

    for file in file_list:
        audio_input = ffmpeg.input(path+'\\'+file)
        video_time = get_length(path+'\\'+file)

        for i in range(int(video_time/20)+1):
            audio_cut = audio_input.audio.filter('atrim', start=i*20, duration=20)
            audio_output = ffmpeg.output(audio_cut, f'./preprocessing_data/{idx}_{i}.mp4', format='mp4', **{'ar': '16000','acodec':'flac'})
            ffmpeg.run(audio_output)

def trim(in_file, out_file, start,end):
    if os.path.exists(out_file):
        os.remove(out_file)
    
    probe_result = ffmpeg.probe(in_file)
    duration = probe_result.get("format",{}).get("duration", None)
    print(duration)

    input_stream = ffmpeg.input(in_file)

    pts = "PTS-STARTPTS"
    video = input_stream.trim(start=start,end=end).setpts(pts)
    audio = (input_stream
             .filter_("atrim",start=start, end=end)
             .filter_("asetpts", pts))
    video_and_audio = ffmpeg.concat(video, audio, v=1, a=1)
    output = ffmpeg.output(video_and_audio, out_file, format="mp4", **{'ar': '16000','acodec':'flac'})
    output.run()

def main():
    file_list = os.listdir(os.getcwd()+'\original_data')
    path = os.getcwd()+'\original_data'
    new_path = os.getcwd()+'\preprocessing_data'
    idx = 0
    for file in file_list:
        video_time = get_length(path+'\\'+file)

        print(video_time)
        print(file)

        print(path+"\\"+file)
        # for i in range(int(video_time/20)+1):
        #     trim(path+"\\"+file, new_path+"\\"+f"{idx}"+f"_{i}.mp4",i*20,(i+1)*20)
        # idx += 1

        trim(path+"\\"+file, new_path+"\\"+f"{idx}"+f".mp4",20,video_time)

main()