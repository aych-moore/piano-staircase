import os
import time

print("script begin")

letters = ['A', 'B', 'C', 'D', 'E', 'F']

for letter in letters:
    for num in range(8):
        os.system('mpg321 audio/piano/' + letter + num + '.mp3 &')
        time.sleep(200)

print("script end")