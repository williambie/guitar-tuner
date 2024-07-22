import os
from config import CHORDS
from audio_recording import record_audio
from audio_processing import read_wav, extract_fundamental_freq

def main():
    while True:
        user_input = input("Enter the string you want to tune (e.g., E, A, D, G, B, e) or 'quit' to exit: ").strip()
        if user_input.lower() == 'quit':
            print("Exiting tuner.")
            break

        if user_input not in CHORDS:
            print("Invalid string. Please enter a valid string.")
            continue

        target_freq = CHORDS[user_input]
        record_audio("output.wav", 5)
        signal, sample_rate = read_wav("output.wav")
        freq = extract_fundamental_freq(signal, sample_rate)
        os.remove("output.wav")
        
        if freq is not None and freq > 0:
            # Check tuning status
            if abs(freq - target_freq) < 1:
                tuning_status = "in tune"
            elif freq < target_freq:
                tuning_status = "flat"
            else:
                tuning_status = "sharp"

            # Print results
            print(f"Detected frequency: {freq:.2f} Hz")
            print(f"Target frequency for {user_input}: {target_freq} Hz")
            print(f"Tuning Status: {tuning_status}")
            print(f"Difference: {abs(freq - target_freq):.2f} Hz ({abs(freq - target_freq) / target_freq * 100:.2f}%)")
            if tuning_status == "in tune":
                print("String is in tune. You can now choose another string or quit.")
        else:
            print("No fundamental frequency detected.")

if __name__ == "__main__":
    main()
