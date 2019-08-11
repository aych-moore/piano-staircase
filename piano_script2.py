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
drum_wavs = ["/home/pi/piano-staircase/audio/drums/" + str(i) + ".wav" for i in [1,7,8,13,11,18,16,5]]
dj_wavs = ["/home/pi/piano-staircase/audio/dj/" + str(i) + ".wav" for i in range(1,8)]


pygame.mixer.init(channels = 8)
pygame.init()
pygame.mixer.music.set_volume(100)

drum_sound = [pygame.mixer.Sound(drum_wavs[i]) for i in range(8)]
dj_tracks = [pygame.mixer.Sound(dj_wavs[i]) for i in range(8)]


def play_drums(message_data):
    for i in range(1,9):
        if(int(message_data[i]) >= 5 and int(message_data[i]) <= 30):
        #if(message_data[i] and not pygame.mixer.Channel(i).get_busy()): # sensor is active and channel empty
            pygame.mixer.Channel(i-1).play(drum_sound[i-1]) #play sound
        
def play_dj(message_data):
    for i in range(1,9):
        if(int(message_data[i]) >= 5 and int(message_data[i]) <= 30):
        #if(message_data[i] and not pygame.mixer.Channel(i).get_busy()): # sensor is active and channel empty
            pygame.mixer.Channel(i).play(dj_tracks[i]) #play sound
    


for i in range(8):
    pygame.mixer.Channel(i).play(drum_sound[i]) #play sound



while 'pigs' != 'flying':
    #print(ser.readline())
    message = ser.readline().decode("utf-8").strip()
    print(message) #message format: "insturment,num"
    message_components = message.split(',') #format: [insturment,num]
    if message_components[0] == '0':
        play_dj(message_components)
