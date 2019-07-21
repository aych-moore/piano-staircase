import pygame
import time

print("script begin")

letters = ['A', 'B', 'C', 'D', 'E', 'F']




for letter in letters:
    for num in range(8):
        pygame.mixer.init()
        pygame.mixer.music.load("audio/piano/" + letter + str(num) + ".mp3")
        pygame.mixer.music.play()
        time.sleep(500)




print("script end")