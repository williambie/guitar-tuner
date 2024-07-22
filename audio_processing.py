import wave
import numpy as np
import librosa

def read_wav(filename):
    # Read the wav file
    with wave.open(filename, "rb") as wf:
        sr = wf.getframerate()
        nframes = wf.getnframes()
        signal = wf.readframes(nframes)
        signal = np.frombuffer(signal, dtype=np.int16)
    return signal, sr

def extract_fundamental_freq(signal, sample_rate):
    # Normalize signal
    signal = signal.astype(np.float32)
    signal = signal / np.max(np.abs(signal))

    # Get pitch using librosa
    pitches = librosa.yin(signal, fmin=50, fmax=500, sr=sample_rate)
    
    # Return the median pitch
    return np.median(pitches)
