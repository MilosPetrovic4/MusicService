import pygame, time, random
from tkinter import *
pygame.mixer.init()

#Stores every song on list to be later accessed by generating a random index
master_song_list = ["GameFiles/Music/terrortech_inc_.xm", "GameFiles/Music/Battle_for_life.xm", "GameFiles/Music/caverns_of_time.xm",
"GameFiles/Music/climax.it", "GameFiles/Music/mystery.xm", "GameFiles/Music/trapped.xm", "GameFiles/Music/battle_of_the_fireflies.s3m",
"GameFiles\Music\TORCS1.mp3", "GameFiles/Music/01 grabbag _ theme from duke nukem 3d.mp3"]


#Chooses a random song by generating a random number
def play_song():
        
    song_selection = random.randrange(0, len(master_song_list) - 1)

    pygame.mixer.music.load(master_song_list[song_selection])
    pygame.mixer.music.play(loops = 0)

#Main loop
root = Tk()
root.title("M's Music Service")
root.geometry("1080x1080")
root.resizable(width=False, height=False)
play_song()
root.mainloop()

