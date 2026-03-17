import numpy as np
def normalize_audio(audio):
    max_val = np.max(np.abs(audio))
    if max_val == 0:
        return audio
    normalized = audio / max_val
    return normalized
