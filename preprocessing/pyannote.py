import platform
import logging
import torchaudio


logger = logging.getLogger(__name__)
current_system = platform.system()
print(current_system)
if current_system == "Windows":
    logger.warning(
        "The torchaudio backend is switched to 'soundfile'. Note that 'sox_io' is not supported on Windows."
    )
    torchaudio.set_audio_backend("soundfile")

# 1. visit hf.co/pyannote/speaker-diarization and hf.co/pyannote/segmentation and accept user conditions (only if requested)
# 2. visit hf.co/settings/tokens to create an access token (only if you had to go through 1.)
# 3. instantiate pretrained speaker diarization pipeline
from pyannote.audio import Pipeline
pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1",
                                    use_auth_token="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")

# 4. apply pretrained pipeline
#diarization = pipeline("C:/ITStudy/3/original_data/1.mp4")
diarization = pipeline("C:/ITStudy/3/preprocessing_data/0_0.wav", num_speakers=2)

# 5. print the result
for turn, _, speaker in diarization.itertracks(yield_label=True):
    print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")
# start=0.2s stop=1.5s speaker_0
# start=1.8s stop=3.9s speaker_1
# start=4.2s stop=5.7s speaker_0
# ...