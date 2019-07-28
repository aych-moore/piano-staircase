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
drum_file_numbers = [1,7,8,13,11,18,16,5]

pygame.mixer.init()
pygame.init()
pygame.mixer.music.set_volume(100)

def play_drums(num):
        print('drums')
        audio_file = "audio/drums/" + str(drum_file_numbers[num]) + ".wav"
        print(audio_file)
        pygame.mixer.Sound(audio_file).play()
        time.sleep(0.5)

def play_piano(num):
        pass

def play_song():
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
for beat in drum_file_numbers:
        audio_file = "audio/drums/" + str(beat) + ".wav"
        drums.append(pygame.mixer.Sound(audio_file))
    

pygame.mixer.set_num_channels(50)


while 'pigs' != 'flying':
        message = ser.readline().strip()
        print(message) #message format: "insturment,num"
        message_components = message.split(b',') #format: [insturment,num]
        print(message_components[1])
        if message_components[0] == b'piano':
                play_piano(message_components[1])
        elif message_components[0] == b'drums':
                play_drums(message_components[1])
        
    

print("script end")