import numpy as np
import librosa
import matplotlib.pyplot as plt
import webrtcvad
import soundfile as sf
import librosa.display
import noisereduce as nr

def vad_with_overlap_detection(audio_file):
    """
    Performs Voice Activity Detection on an audio file.

    Args:
        audio_file (str): Path to the audio file.
    
    Returns:
        Plots the waveform and VAD result of the Audio File
    """
    # Load the audio file
    y, sr = librosa.load(audio_file, sr=None)
    y = librosa.to_mono(y)
    y = nr.reduce_noise(y=y, sr=sr)
    # Ensure the audio is mono
    if len(y.shape) > 1:
        y = np.mean(y, axis=1)

    # Resample to 16000 Hz
    if sr != 16000:
        y = librosa.resample(y, orig_sr=sr, target_sr=16000)
        sr = 16000

    # Create a VAD object
    vad = webrtcvad.Vad()

    # Set its aggressiveness mode
    vad.set_mode(0)

    # Convert the float audio data to int16
    y = (y * 32767).astype(np.int16)

    # Frame the audio data
    frame_duration = 0.02  # 20 ms
    frame_length = int(sr * frame_duration)
    frames = [y[i:i+frame_length] for i in range(0, len(y), frame_length)]

    # Apply VAD on each frame
    is_speech = [vad.is_speech(frame.tobytes(), sr) for frame in frames]


    # Plot the waveform and VAD result
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(y)
    plt.title('Waveform')
    plt.subplot(2, 1, 2)
    plt.plot(is_speech)
    plt.title('VAD Result')
    plt.tight_layout()
    plt.show()


# Replace 'your_audio_file.wav' with the path to your audio file
audio_file_path = 'iisc_1.mp3'

# Run VAD with overlap detection and plot the graph
vad_with_overlap_detection(audio_file_path)