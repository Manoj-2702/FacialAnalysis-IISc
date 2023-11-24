# Voice Activity Detection with Overlap Detection

This project uses the WebRTC VAD module to perform Voice Activity Detection (VAD) on an audio file. It also applies noise reduction to the audio file before performing VAD.

## Dependencies

- Python 3
- numpy
- librosa
- matplotlib
- webrtcvad
- soundfile
- noisereduce

You can install these dependencies using pip:

```bash
pip install numpy librosa matplotlib webrtcvad soundfile noisereduce
```

or

```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repo

```bash
    git clone https://github.com/Manoj-2702/FacialAnalysis-IISc.git
```

2. Navigate to the directory

```bash
    cd FacialAnalysis-IISc/OverlappedSpeech
```

3. Run the script

```
    python vad.py
```

```python
from vad import vad_with_overlap_detection

# Replace 'your_audio_file.wav' with the path to your audio file
audio_file_path = 'your_audio_file.wav'

# Run VAD with overlap detection and plot the graph
vad_with_overlap_detection(audio_file_path)

```

4. The output will be a graph showing the overlapping speech regions.

## Audio File

Sample audio file is in this repo. iisc_1.mp3


https://github.com/Manoj-2702/FacialAnalysis-IISc/blob/main/OverlappedSpeech/Overlapped_Speech_Graph.png
