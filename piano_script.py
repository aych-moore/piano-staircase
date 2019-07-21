import pygame
import time

print("script begin")

letters = ['A', 'B', 'C', 'D', 'E', 'F']

pygame.mixer.init()



for letter in letters:
    for num in range(8):
        pygame.mixer.music.load("audio/piano/" + letter + str(num) + "5.mp3")
        pygame.mixer.music.play()
        time.sleep(200)




print("script end")