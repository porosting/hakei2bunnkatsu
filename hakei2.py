import librosa.display
import matplotlib.pyplot as plt

from hakei1 import wav,sr

plt.figure(figsize=(15, 5))
librosa.display.waveshow(wav, sr)
plt.show()