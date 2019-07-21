import pygame
import time
from pygame.locals import *

print("script begin")

letters = ['A', 'B', 'C', 'D', 'E', 'F']

pygame.mixer.music.load("C5.mp3")
pygame.mixer.music.play()

"""
for letter in letters:
    for num in range(8):
        os.system('mpg321 audio/piano/' + letter + str(num) + '.mp3 &')
        time.sleep(200)
"""
print("script end")