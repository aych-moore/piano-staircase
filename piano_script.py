import pygame
import time
import random

print("script begin")

letters = ['A', 'B', 'C', 'D', 'E', 'F']

pygame.mixer.init()
pygame.init()

sounds = []
for letter in letters:
    for num in range(1,8):
        audio_file = "audio/piano/" + letter + str(num) + ".wav"
        sounds.append(pygame.mixer.Sound(audio_file))
    

pygame.mixer.set_num_channels(50)
"""
for sound in sounds:
    print("PLAYING SOUND")
    sound.play()
    time.sleep(0.2)
"""
while True:
    random_time = random.randint(10,100)*0.01
    for i in range(random.randint(1,5)):
        random.choice(sounds).play()
        time.sleep(random_time)

print("script end")