# vocie-phishing-predict

## 대화내용을 입력으로 받아 해당 대화가 보이스피싱 대화인지 분류

### preprocessing/
audio_split_librosa.py 
- librosa 라이브러리릉 통해 audio data의 sample rate를 변경하고 speaker diarization을 통해 speaker를 분리시키기 위한 코드

audio_split_ffmpeg.py
- ffmpeg 라이브러리릉 통해 audio data의 sample rate를 변경하고 speaker diarization을 통해 speaker를 분리시키기 위한 코드

stt_etri.py
- audio_split.py를 통해 전처리한 음성(Speech) 데이터를 etri 음성인식 api를 호출해 텍스트로 변환시키기 위한 코드

text_to_csv.py
- 텍스트로 변환한 데이터를 csv파일에 저장하는 코드
