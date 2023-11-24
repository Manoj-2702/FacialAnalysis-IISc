# from pyannote.audio import Pipeline
from pyannote.audio.pipelines import OverlappedSpeechDetection
from dotenv import load_dotenv
import os
load_dotenv()

hugging_face_token=os.environ.get("HUGGING_FACE_TOKEN")
pipeline = OverlappedSpeechDetection.from_pretrained("pyannote/overlapped-speech-detection",use_auth_token=hugging_face_token)
audio_file_path = "IIsc_Voice_Sample.mp3"

output = pipeline({'uri': 'filename', 'audio': audio_file_path})

for speech in output['uri'].get_timeline().itertracks():
    # Two or more speakers are active between speech.start and speech.end
    print(f"Overlapped Speech Detected: {speech.start} - {speech.end}")

