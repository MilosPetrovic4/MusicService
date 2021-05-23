import pygame, time, random
from tkinter import *
from tkinter import filedialog
from PIL import Image
pygame.mixer.init()
pygame.mixer.music.set_volume(4/10) #Default setting
pause_unpause = 0 #Used to logically determine whether to pause or unpause music 

#Stores every song on list to be later accessed by generating a random index
master_song_list = ["GameFiles/Music/terrortech_inc_.xm", "GameFiles/Music/Battle_for_life.xm", "GameFiles/Music/caverns_of_time.xm",
"GameFiles/Music/climax.it", "GameFiles/Music/mystery.xm", "GameFiles/Music/trapped.xm", "GameFiles/Music/battle_of_the_fireflies.s3m",
"GameFiles/Music/TORCS1.mp3", "GameFiles/Music/01 grabbag _ theme from duke nukem 3d.mp3", "GameFiles/Music/crypt.xm", "GameFiles/Music/szc2_-_fight_for_your_lives.xm"
, "GameFiles/Music/forbidden_zone.mod", "GameFiles/Music/technology.xm"]

#Adds the songs from the master song list to the list widget
def insert_to_song_list():
    for i in range(0, len(master_song_list), 1):
        list_song = master_song_list[i]
        list_song = list_song.split('/')[-1]  #.split('.')[0] --> removes file type which prevents song from running
        song_list.insert(END, list_song)

#Global pause variable
global paused
paused = False

#pause and unpauses music
def pause(is_paused):
    global paused
    paused = is_paused

    if paused: #if paused is true the if statement is true
        pygame.mixer.music.unpause()
        paused = False

    else:
        pygame.mixer.music.pause()
        paused = True

#Stops playing current song
def stop_music():
    pygame.mixer.music.stop()
    song_list.select_clear(ACTIVE)

#Play the next song
def next_song():
    #Receives the current song as a tuple number
    next_one = song_list.curselection()

    #Add one to song
    next_one = next_one[0]+1

    #Get title of th song
    song = song_list.get(next_one)

    #Plays next song
    pygame.mixer.music.load(f'GameFiles/Music/{song}')
    pygame.mixer.music.play(loops=0)

    #Move active bar in playlist
    song_list.select_clear(0, END)
    #activate new bar
    song_list.activate(next_one)

    #set active bar 
    song_list.selection_set(next_one, last=None)

#Play previous song
def previous_song():
    #Receives the current song as a tuple number
    previous_one = song_list.curselection()

    #Subtract one to song
    previous_one = previous_one[0]-1

    #Get title of the song
    song = song_list.get(previous_one)

    #Plays next song
    pygame.mixer.music.load(f'GameFiles/Music/{song}')
    pygame.mixer.music.play(loops=0)

    #Move active bar in playlist
    song_list.select_clear(0, END)
    #activate new bar
    song_list.activate(previous_one)

    #set active bar 
    song_list.selection_set(previous_one, last=None)    

#Plays song that was clicked on in listbox
def play_selected():
    song = song_list.get(ACTIVE)
    selected_song = f'GameFiles/Music/{song}'
    pygame.mixer.music.load(selected_song)
    pygame.mixer.music.play(loops=0)

#Receives input from scale widget which is used to calculate new volume
def get_music_volume(event):
    slider_value = music_slider.get()
    pygame.mixer.music.set_volume(slider_value/10)

#add song function
def add_song():
    new_song_path = filedialog.askopenfilename(initialdir='GameFiles/Music/', title="Choose Song") #filetypes=(("xm Files", "*.xm"), ("mp3 Files", "*.mp3"), ("IT Files", "*.it"))
    #Not really sure how this works but essentially extracts only the name of the song
    new_song = new_song_path.split('/')[-1] #.split('.')[0] --> removes file type which prevents song from running
    song_list.insert(END, new_song) #Adds the newly inserted song to list box

#Add multiple songs at once
def multiple_songs():
    new_song_path = filedialog.askopenfilenames(initialdir='GameFiles/Music/', title="Choose Song")

    #replaces directory info for list of new songs
    for songs in new_song_path:
        new_song = new_song_path.split('/')[-1]
        song_list.insert(END, new_song) #Adds the newly inserted song to list box
        
#Delete a song
def delete_song():
    song_list.delete(ANCHOR) #Deletes selected song
    pygame.mixer.music.stop()

#Delete every song
def delete_all():
    song_list.delete(0, END) #Deletes all songs in the range
    pygame.mixer.music.stop()

#Main loop
root = Tk()
root.title("Milos Music Service")
root.geometry("500x300")
root.resizable(width=False, height=False)

#Listbox
song_list = Listbox(root, bg="black", fg="white",width=60, selectbackground="gray", selectforeground="black", borderwidth=10)
song_list.place(bordermode=OUTSIDE, x=50,y=40)
insert_to_song_list() #--> Adds all songs that are manually in the program

#Music volume slider
music_slider = Scale(root, from_=1, to=10, borderwidth=0, orient=VERTICAL, troughcolor="grey", length=180, width=20, command=get_music_volume)
music_slider.set(4)
music_slider.place(bordermode=OUTSIDE, x=435, y=40)

#Define Player Control Button Images
play_btn_img = PhotoImage(file="GameFiles/Images/play button.png")
pause_btn_img = PhotoImage(file="GameFiles/Images/pause button.png")
stop_btn_img = PhotoImage(file="GameFiles/Images/stop button.png")
back_btn_img = PhotoImage(file="GameFiles/Images/back button.png")
forward_btn_img = PhotoImage(file="GameFiles/Images/forward button.png")

#Create Player control Buttons
back_button = Button(image=back_btn_img, borderwidth=0, command=previous_song)
stop_button = Button(image=stop_btn_img, borderwidth=0, command=stop_music)
play_button = Button(image=play_btn_img, borderwidth=0, command=play_selected)
pause_button = Button(image=pause_btn_img, borderwidth=0, command=lambda: pause(paused)) #lambda: pause() passes in the paused global variable in the brackets (only tkinter uses lambda)
forward_button = Button(image=forward_btn_img, borderwidth=0, command=next_song)

#Place buttons on grid
y_buttons = 230
back_button.place(bordermode=OUTSIDE, x=70, y=y_buttons)
pause_button.place(bordermode=OUTSIDE, x=140, y=y_buttons)
play_button.place(bordermode=OUTSIDE, x=210, y=y_buttons)
stop_button.place(bordermode=OUTSIDE, x=280, y=y_buttons)
forward_button.place(bordermode=OUTSIDE, x=350, y=y_buttons)

#Create new menu
player_menu = Menu(root)
root.config(menu=player_menu)

#Add song menu option
add_song_menu = Menu(player_menu)
player_menu.add_cascade(label="Add", menu=add_song_menu)
add_song_menu.add_command(label="Open File", command=add_song)

#add multiple songs to playlist
add_song_menu.add_command(label="Open Multiple Files", command=multiple_songs)

#Create song delete meny
remove_song_menu = Menu(player_menu)
player_menu.add_cascade(label="Remove", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete File", command=delete_song)
remove_song_menu.add_command(label="Delete Multiple Files", command=delete_all)

root.mainloop()




