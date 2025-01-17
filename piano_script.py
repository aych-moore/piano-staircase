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

time.sleep(4); #wait 4 seconds to give system time to init

letters = ['A', 'B', 'C', 'D', 'E', 'F']
drum_file_numbers = [1,7,8,13,11,18,16,5]



pygame.mixer.init(channels = 9)
pygame.init()
pygame.mixer.music.set_volume(100)

def play_drums(num):
        audio_file = "/home/pi/piano-staircase/audio/drums/" + str(drum_file_numbers[num]) + ".wav"
        print(audio_file)
        pygame.mixer.Sound(audio_file).play()
        time.sleep(0.5)

def play_piano(num):
        audio_file = "/home/pi/piano-staircase/audio/piano/" + 'C' + str(num+1) + ".wav"
        print(audio_file)
        pygame.mixer.Sound(audio_file).play()
        time.sleep(0.5)

def play_song():
        random_time = random.randint(1,60)*0.01
        for i in range(random.randint(1,10)):
                random.choice(sounds).play()
                time.sleep(random_time)


"""Generate a list of playable sounds"""
sounds = []
for letter in letters:
    for num in range(1,8):
        audio_file = "/home/pi/piano-staircase/audio/piano/" + letter + str(num) + ".wav"
        sounds.append(pygame.mixer.Sound(audio_file))
drums = []
for beat in drum_file_numbers:
        audio_file = "/home/pi/piano-staircase/audio/drums/" + str(beat) + ".wav"
        drums.append(pygame.mixer.Sound(audio_file))
    



while 'pigs' != 'flying':
        message = ser.readline().decode("utf-8").strip()
        print(message) #message format: "insturment,num"
        message_components = message.split(',') #format: [insturment,num]
        if message_components[0] == '0':
                play_piano(int(message_components[1]))
        elif message_components[0] == '1':
                play_drums(int(message_components[1]))
