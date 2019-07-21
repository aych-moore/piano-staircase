import time
import pygame

print("script begin")

letters = ['A', 'B', 'C', 'D', 'E', 'F']

pygame.mixer.init()
pygame.mixer.music.load("C5.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue


"""
for letter in letters:
    for num in range(8):
        os.system('mpg321 audio/piano/' + letter + str(num) + '.mp3 &')
        time.sleep(200)
"""
print("script end")