import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv 



sampling_frequency = 48000
recording_duration = float(input("How many seconds do you wish to record for?: "))
channels = 1

print("Recording has begun please begin speaking into mic")
print(f"Recording time remaining: ")
recording = sd.rec(int(recording_duration*sampling_frequency), samplerate=sampling_frequency, channels=channels)

sd.wait()

import time
import sys

def countdown(t):
    while t >= 0:
        # Convert total seconds into minutes and seconds
        mins, secs = divmod(t, 60)
        # Format the time string with leading zeros (e.g., 05:02)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        
        # Print the time on the same line, overwriting the previous output
        sys.stdout.write('\rTime left: ' + timer)
        sys.stdout.flush() # Forces the output to be displayed immediately
        
        # Pause the loop for 1 second
        time.sleep(1)
        
        # Decrease the time by 1 second
        t -= 1
    
    # After the loop finishes (t reaches 0), print a final message on a new line
    print('\nTimes up!!!')
