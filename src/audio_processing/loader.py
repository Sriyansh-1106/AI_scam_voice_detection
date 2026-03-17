import librosa 
import numpy as np

def load_audio(file_path):
    audio, sample_rate = librosa.load(file_path, sr=None)
    return audio, sample_rate