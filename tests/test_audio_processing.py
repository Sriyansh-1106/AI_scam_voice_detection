import pytest
import numpy as np
import os

def test_load_audio_returns_data():
    from src.audio_processing.loader import load_audio

    test_file = "tests/test_data/sample.wav"

    audio, sample_rate = load_audio(test_file)

    assert audio is not None
    assert len(audio) > 0
    assert sample_rate > 0
    


def test_normalize_audio_returns_correct_range():
    from src.audio_processing.loader import load_audio
    from src.audio_processing.normalizer import normalize_audio

    audio, sample_rate = load_audio("tests/test_data/sample.wav")

    normalized = normalize_audio(audio)

    assert np.max(normalized) <= 1.0
    assert np.min(normalized) >= -1.0