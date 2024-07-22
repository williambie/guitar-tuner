import pyaudio

# Constants for recording
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Frequencies for guitar strings
CHORDS = {
    'E': 82.41,  # Low E string
    'A': 110.00, # A string
    'D': 146.83, # D string
    'G': 196.00, # G string
    'B': 246.94, # B string
    'e': 329.63  # High E string
}
