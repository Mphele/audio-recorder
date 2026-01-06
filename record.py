import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv 
import time
import sys
import numpy as np
import os
from pathlib import Path

sampling_frequency = 48000
filename = input("What do you wish to name the recording file?: ")
recording_duration = float(input("How many seconds do you wish to record for?: "))
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
recording = sd.rec(int(recording_duration*sampling_frequency), samplerate=sampling_frequency, channels=channels)
countdown(recording_duration)
sd.wait()
print()
print("Recording finished.")

def find_file_anywhere(filename, search_path='/'):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

wv.write(f"{filename}.wav", recording, sampling_frequency,sampwidth=2)
file_to_find = f"{filename}.wav"
found_location = find_file_anywhere(file_to_find, search_path= os.getcwd()) 

print(f"Audio file saved as {filename}.wav at {found_location}")


