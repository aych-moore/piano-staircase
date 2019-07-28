import pygame
import time
import random
import serial

ser = serial.Serial(
               port='/dev/ttyUSB0',
               baudrate = 9600,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               bytesize=serial.EIGHTBITS,
               timeout=1
           )

print("script begin")

letters = ['A', 'B', 'C', 'D', 'E', 'F']
numbers = [1,7,8,13,11,18,16,5]

pygame.mixer.init()
pygame.init()
pygame.mixer.music.set_volume(100)

def play_drum(note):
        pass

def play_piano(note):
        random_time = random.randint(1,60)*0.01
        for i in range(random.randint(1,10)):
                random.choice(sounds).play()
                time.sleep(random_time)


"""Generate a list of playable sounds"""
sounds = []
for letter in letters:
    for num in range(1,8):
        audio_file = "audio/piano/" + letter + str(num) + ".wav"
        sounds.append(pygame.mixer.Sound(audio_file))
drums = []
for beat in numbers:
        audio_file = "audio/drums/" + str(beat) + ".wav"
        drums.append(pygame.mixer.Sound(audio_file))
    

pygame.mixer.set_num_channels(50)

"""
for beat in drums:
        beat.play()
        time.sleep(1.5)
"""

while 'pigs' != 'flying':
        x=ser.readline()
        print(x)
    

print("script end")