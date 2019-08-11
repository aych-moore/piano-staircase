import pygame
import time

print("begin")

#-----------------------------------------init
piano_wavs = []
drum_wavs = ["audio/drums/" + str(i) + ".wav" for i in [1,7,8,13,11,18,16,5]]
dj_wavs = ["audio/dj/foundation.wav"] + ["audio/dj/" + str(i) + ".wav" for i in range(1,8)]

print(drum_wavs)
print(dj_wavs)


pygame.mixer.init(channels = 9)
pygame.init()
pygame.mixer.music.set_volume(100)

#make sound objects
foundation = pygame.mixer.Sound(dj_wavs[0])
dj_tracks = [pygame.mixer.Sound(dj_wavs[i]) for i in range(1,8)]

#play all tracks
pygame.mixer.Channel(0).play(foundation, loops=-1) #play foundation
for i in range(1,8):
    pygame.mixer.Channel(i).play(dj_tracks[i-1], loops=-1) #play track
    dj_tracks[i-1].set_volume(0) #mute all tracks


foundation.set_volume(0)
dj_tracks[1].set_volume(1)
dj_tracks[2].set_volume(1)


"""
time.sleep(3)
pygame.mixer.Channel(1).play(dj_tracks[0])
time.sleep(2)
foundation.set_volume(0)
time.sleep(2)
foundation.set_volume(1)
"""



#-----------------------------------------main loop
#while("shwoop" != "not shwooping"): 
    



