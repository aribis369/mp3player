from tkinter import *
from tkinter import filedialog
import os
import pygame
import numpy as np
import pandas as pd

master = Tk()
master.minsize(360,70)
master.title("AB369Player")

pi=0
trkno = 0
songs = []
def browse():
    global songs
    global dir
    dir=filedialog.askdirectory()
    os.chdir(dir)
    for song in os.listdir(dir):
        if song.endswith(".mp3"):
            songs.append(song)
    for index,song in enumerate(songs):
        print('{}. {}'.format(index,song))
    pygame.mixer.init()
    if len(songs)>=1:
        try:
            pygame.mixer.music.load(songs[0])
        except IndexError:
            print('Please select a song!')

def play():
    global trkname
    global trkno
    global pi
    if pi==0:
        pygame.mixer.music.play()
        trkname.set((str(songs[trkno])).replace(".mp3",""))
    else:
        pygame.mixer.music.unpause()

def stop():
    global pi
    pygame.mixer.music.pause()
    pi=1

def nexttrk():
    global trkname
    global trkno
    global songs
    trkno += 1
    pygame.mixer.music.load(songs[trkno])
    pygame.mixer.music.play()
    trkname.set((str(songs[trkno])).replace(".mp3",""))

def prevtrk():
    global trkname
    global trkno
    global songs
    trkno -= 1
    pygame.mixer.music.load(songs[trkno])
    pygame.mixer.music.play()
    trkname.set((str(songs[trkno])).replace(".mp3",""))

def voli():
    global vol
    vol=pygame.mixer.music.get_volume()
    vol += 0.1
    if vol>=0.9921875:
        vol = 0.9921875
    pygame.mixer.music.set_volume(vol)

def vold():
    global vol
    vol=pygame.mixer.music.get_volume()
    vol -= 0.1
    if vol<0:
        vol = 0.0
    pygame.mixer.music.set_volume(vol)


font1='Courier', 25, 'bold'
font2='Courier', 15, 'bold'

trkname=StringVar()
pi = 0
vol = 1
Button(master,text='>>|',command=nexttrk).grid(row=1,column=3,sticky=W,pady=4)
Button(master,text='|<<',command=prevtrk).grid(row=1,column=0,sticky=W,pady=4)
Button(master,text='||',command=stop).grid(row=1,column=1,sticky=W,pady=4)
Button(master,text='>',command=play).grid(row=1,column=2,sticky=W,pady=4)
Label(master,textvariable=trkname,font=font1).grid(row=1,column=4)
Button(master,text=' + ',command=voli).grid(row=2,column=0,sticky=W,pady=4)
Button(master,text=' - ',command=vold).grid(row=2,column=3,sticky=W,pady=4)
Button(master,text='Browse',command=browse).grid(row=2,column=4,sticky=W,pady=4)

master.mainloop()
