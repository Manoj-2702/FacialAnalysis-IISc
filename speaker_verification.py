import torch
from pyannote.audio.pipelines.speaker_verification import PretrainedSpeakerEmbedding
model = PretrainedSpeakerEmbedding(
    "speechbrain/spkrec-ecapa-voxceleb",
    device=torch.device("cuda" if torch.cuda.is_available() else "cpu"))

from pyannote.audio import Audio
from pyannote.core import Segment
audio = Audio(sample_rate=16000, mono="downmix")

# extract embedding for a speaker speaking between t=3s and t=6s
speaker1 = Segment(327., 338.)
waveform1, sample_rate = audio.crop("IISc_Voice_Sample.mp3", speaker1)
embedding1 = model(waveform1[None])

# extract embedding for a speaker speaking between t=7s and t=12s
speaker2 = Segment(341., 345.)
waveform2, sample_rate = audio.crop("IISc_Voice_Sample.mp3", speaker2)
embedding2 = model(waveform2[None])

# compare embeddings using "cosine" distance
from scipy.spatial.distance import cdist
distance = cdist(embedding1, embedding2, metric="cosine")
print(distance)

if distance[0][0]<0.4:
    print("It is the same Speaker")
else:
    print("The speaker is different")
