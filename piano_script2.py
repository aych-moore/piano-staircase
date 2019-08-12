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

interaction_count = 0 #counts interactions

letters = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']

piano_wavs = ["/home/pi/piano-staircase/audio/piano/" + note + ".wav" for note in letters]
drum_wavs = ["/home/pi/piano-staircase/audio/drums/" + str(i) + ".wav" for i in [1,7,8,13,11,18,16,5]]


pygame.mixer.init(channels = 8)
pygame.init()
pygame.mixer.music.set_volume(100)

drum_sound = [pygame.mixer.Sound(drum_wavs[i]) for i in range(8)]
piano_sound = [pygame.mixer.Sound(piano_wavs[i]) for i in range(8)]

def log_interaction():
    interaction_count += 1
    if(interaction_count >= 10):
        f = open( 'interaction_log.txt', 'a')
        f.write("X")
        f.close()

def play_drums(message_data):
    for i in range(1,9):
        if(int(message_data[i]) >= 5 and int(message_data[i]) <= 130):
        #if(message_data[i] and not pygame.mixer.Channel(i).get_busy()): # sensor is active and channel empty
            pygame.mixer.Channel(i-1).play(drum_sound[i-1]) #play sound
            log_interaction()

def play_piano(message_data):
    for i in range(1,9):
        if(int(message_data[i]) >= 5 and int(message_data[i]) <= 130):
            if(not pygame.mixer.Channel(i-1).get_busy()): # sensor is active and channel empty
                pygame.mixer.Channel(i-1).play(piano_sound[i-1]) #play sound
                log_interaction()



while 'pigs' != 'flying':
    try:
        message = ser.readline().decode("utf-8").strip()
        print(message) #message format: "insturment,num"
        message_components = message.split(',') #format: [insturment,num]
        if message_components[0] == '0':
            play_piano(message_components)
    except:
        pass
