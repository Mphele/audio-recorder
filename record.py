import sounddevice as sd
import wavio as wv 
import time
import sys
import os
sampling_frequency = 48000

filename = input("What do you wish to name the recording file?: ")
if os.path.exists(f'{filename}.wav'):
        while True:
            overwrite = input(f"An audio with the name {filename} already exists in this directory, do you want to rename (R) your current file or overwrite (O) the existing one?: ").lower()
            if overwrite not in ['o', 'r']:
                print("Please either enter 'O' for overwrite or 'R' for rename")
                continue
            break
        if overwrite == 'r':
            while True:
                filename = input("What is the new name you wish to give the file?: ")
                if os.path.exists(f'{filename}.wav'):
                    print("Filename already exists please enter unique filename")
                    continue
                break
        if overwrite == 'o':
            print("File overwritten")



while True:
    try:
        recording_duration = float(input("How many seconds do you wish to record for?: "))
        if recording_duration <= 0:
            print("Recording duration must be greater than 0 seconds.")
            continue
        break
    except ValueError:
        print("Please enter a valid number for duration.")
channels = 1

def countdown(t):
    while t > 0:
        secs = int(t)
        timer = f'{secs:02d}'
        
        
        sys.stdout.write('\r' + "Recording time remaining: "+ timer)
        sys.stdout.flush()
        time.sleep(1) 
        t -= 1


print("Recording has begun please begin speaking into mic")

try:
    recording = sd.rec(
        int(recording_duration * sampling_frequency),
        samplerate=sampling_frequency,
        channels=channels
    )
    countdown(recording_duration)
    sd.wait()
    print("\nRecording finished.")
except Exception as e:
    print("\nRecording failed.")
    print(f"Error: {e}")
    sys.exit(1)


def find_file_anywhere(filename, search_path='/'):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

wv.write(f"{filename}.wav", recording, sampling_frequency,sampwidth=2)
file_to_find = f"{filename}.wav"
found_location = find_file_anywhere(file_to_find, search_path= os.getcwd()) 

print(f"Audio file saved as {filename}.wav at {found_location}")

while True:
    playback = input("Do you want to playback the audio you just saved?(yes/no): ").lower()
    if playback not in ['yes', 'no']:
        print("Please enter either yes or no")
        continue
    break

if playback =='yes':
    print("Playing recording...")
    sd.play(recording,sampling_frequency)
    sd.wait()
    print("Playback finished.")




