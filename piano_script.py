import pygame
import time

print("script begin")

letters = ['A', 'B', 'C', 'D', 'E', 'F']

pygame.mixer.init()
pygame.init()
pygame.mixer.set_num_channels(50)

for letter in letters:
    for num in range(8):
        audio_file = "audio/piano/" + letter + str(num) + ".mp3"
        print("PLAYING: " + audio_file)
        
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        time.sleep(500)




print("script end")