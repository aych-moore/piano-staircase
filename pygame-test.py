import pygame
import time

print("begin")

#-----------------------------------------init
piano_wavs = []
drum_wavs = ["audio/drums/" + str(i) + ".wav" for i in [1,7,8,13,11,18,16,5]]
dj_wavs = ["audio/dj/f" + str(i) + ".wav" for i in range(1,4)] + ["audio/dj/" + str(i) + ".wav" for i in range(1,9)]

print(drum_wavs)
print(dj_wavs)


pygame.mixer.pre_init(44100, 16, 12, 4096) #frequency, size, channels, buffersize
pygame.init() #turn all of pygame on.
pygame.mixer.music.set_volume(100)

display = pygame.display.set_mode((400, 300)) #doesn't work without display. idk why

#make sound objects
#foundations = [pygame.mixer.Sound(dj_wavs[i]) for i in range(0,3)]
dj_tracks = [pygame.mixer.Sound(dj_wavs[i]) for i in range(3,11)]


#play all tracks

"""
for i in range(3):
    pygame.mixer.Channel(i).play(foundations[i], loops=-1) #play foundation
    foundations[i].set_volume(1) #mute all tracks
"""

for i in range(8):
    pygame.mixer.Channel(i).play(dj_tracks[i], loops=-1) #play track
    dj_tracks[i].set_volume(0) #mute all tracks


#time.sleep(2)
dj_tracks[7].set_volume(1)


"""
dj_tracks[0].set_volume(1)
dj_tracks[1].set_volume(1)
dj_tracks[2].set_volume(1)
dj_tracks[3].set_volume(1)
dj_tracks[4].set_volume(1)
dj_tracks[5].set_volume(1)
dj_tracks[6].set_volume(1)
dj_tracks[7].set_volume(1)
"""


#-----------------------------------------main loop
while("shwoop" != "not shwooping"):
    pass
    



