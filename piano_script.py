import time
from pygame import mixer

print("script begin")

letters = ['A', 'B', 'C', 'D', 'E', 'F']

sound = mixer.Sound('audio/piano/C5.mp3')
sound.play()

"""
for letter in letters:
    for num in range(8):
        os.system('mpg321 audio/piano/' + letter + str(num) + '.mp3 &')
        time.sleep(200)
"""
print("script end")