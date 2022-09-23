from tkinter import *
import pygame
import os

root = Tk()
root.title('music player')
root.geometry("500x300")

pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)


songs = []
current_song = ""
paused = False
def load_music():
    global current_song

    root.directory = Music.askdirectory()
    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)

    for song in songs:
        songlist.insert("end", song)

    songlist.selection_get(0)
    current_song = songs[songlist.curselection()[0]]

def play_music():
    global current_song, paused

    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False
def pause_music():
    global pause
    pygame.mixer.music.pause()
    paused = True

def next_music():
    global current_song, paused

    try:
        songlist.selection_clear(0, END)
        songlist.selection_get(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass
def prev_music():
    global current_song, paused

    try:
        songlist.selection_clear(0, END)
        songlist.selection_get(songs.index(current_song) - 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

organise_menu = Menu(menubar)
organise_menu.add_command(label='select folder', command=load_music)
menubar.add_cascade(label='Organise', menu=organise_menu)

songlist = Listbox(root, bg="black", fg="white", width=100, height=15)
songlist.pack()

next_image = PhotoImage(file='next.png')
pause_image = PhotoImage(file='pause.png')
play_image = PhotoImage(file='play.png')
previous_image = PhotoImage(file='previous.png')

control_frame = Frame(root)
control_frame.pack()

next_bth = Button(control_frame, image=next_image, borderwidth=0, command=play_music)
pause_bth = Button(control_frame, image=pause_image, borderwidth=0, command=pause_image)
play_bth = Button(control_frame, image=play_image, borderwidth=0, command=next_music)
previous_bth = Button(control_frame, image=previous_image, borderwidth=0, command=prev_music)

play_bth.grid(row=0, column=1, padx=7, pady=10)
pause_bth.grid(row=0, column=2, padx=7, pady=10)
play_bth.grid(row=0, column=3, padx=7, pady=10)
previous_bth.grid(row=0, column=4, padx=7, pady=10)

root.mainloop()