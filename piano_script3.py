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

MIN_SENSE_RANGE = 5
MAX_SENSE_RANGE = 20

interaction_count = 0 #counts interactions
current_mode = 0

letters = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']

piano_wavs = ["/home/pi/piano-staircase/audio/piano/" + note + ".wav" for note in letters]
drum_wavs = ["/home/pi/piano-staircase/audio/drums/" + str(i) + ".wav" for i in [1,7,8,13,11,18,16,5]]
dj_wavs = ["/home/pi/piano-staircase/audio/dj/" + str(i) + ".wav" for i in range(1,9)]

"""
pygame.mixer.pre_init(44100, 16, 8, 4096) #frequency, size, channels, buffersize
pygame.init() #turn all of pygame on.
pygame.mixer.music.set_volume(100)
#display = pygame.display.set_mode((400, 300)) #doesn't work without display. idk why
"""


pygame.mixer.init(channels = 17)
pygame.init()
pygame.mixer.music.set_volume(100)



#make sound objects
dj_tracks = [pygame.mixer.Sound(dj_wavs[i]) for i in range(8)]
drum_sound = [pygame.mixer.Sound(drum_wavs[i]) for i in range(8)]
piano_sound = [pygame.mixer.Sound(piano_wavs[i]) for i in range(8)]

def log_interaction():
    interaction_count += 1
    print("LOG")
    """
    if(interaction_count >= 2):
        f = open( '/home/pi/piano-staircase/interaction_log.txt', 'a')
        f.write("C")
        f.close()
        interaction_count = 0
        """

def play_drums(message_data):
    for i in range(1,9):
        if(int(message_data[i]) >= MIN_SENSE_RANGE and int(message_data[i]) <= MAX_SENSE_RANGE):
            if(not pygame.mixer.Channel(i-1).get_busy()): # sensor is active and channel empty
                interaction_count += 1
                pygame.mixer.Channel(i-1).play(drum_sound[i-1]) #play sound
                

def play_piano(message_data):
    for i in range(1,9):
        if(int(message_data[i]) >= MIN_SENSE_RANGE and int(message_data[i]) <= MAX_SENSE_RANGE):
            if(not pygame.mixer.Channel(i-1).get_busy()): # sensor is active and channel empty
                interaction_count += 1
                pygame.mixer.Channel(i-1).play(piano_sound[i-1]) #play sound
                

def play_piano2(message_data):
    for i in range(1,9):
        if(int(message_data[i]) >= MIN_SENSE_RANGE and int(message_data[i]) <= MAX_SENSE_RANGE):
            interaction_count += 1
            pygame.mixer.Channel(i-1).play(piano_sound[i-1]) #play sound
            

def play_dj(message_data):
    for i in range(1,9):
        if(int(message_data[i]) >= MIN_SENSE_RANGE and int(message_data[i]) <= MAX_SENSE_RANGE):
            interaction_count += 1
            pygame.mixer.Channel(i-1).set_volume(0.1) #unmte
        else:
            pygame.mixer.Channel(i-1).set_volume(0) #mute
            

            

def stop_all_channels():
    for i in range(0,8):
        pygame.mixer.Channel(i).stop() #mute all tracks


#pygame.mixer.Channel(0).play(dj_tracks[0], loops=-1) #play track
#pygame.mixer.Channel(0).set_volume(0.1) #mute all tracks

while 'pigs' != 'flying':
    print(interaction_count)
    try:
        message = ser.readline().decode("utf-8").strip()
        print(message) #message format: "insturment,num"
        message_components = message.split(',') #format: [insturment,num]
        if message_components[0] == '0': #mode
            current_mode = 0
            play_piano(message_components)
        if message_components[0] == '1': #mode
            current_mode = 1
            play_drums(message_components)
        if message_components[0] == '3': #mode
            current_mode = 2
            play_piano2(message_components)


        if message_components[0] == '2': #mode
            if(current_mode != 2): #if this is the first time on mode 2 from another mode
                for i in range(8): #play all tracks quietly
                    pygame.mixer.Channel(i).play(dj_tracks[i], loops=-1) #play track
                    pygame.mixer.Channel(i).set_volume(0) #mute all tracks
            current_mode = 2
            play_dj(message_components)

    except:
        pass
