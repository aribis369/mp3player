from Tkinter import *
import os
import pygame
import tkFileDialog



master=Tk()
master.minsize(300,50)
master.title("AB369Player")

trkno=0
songs=[]
dir=tkFileDialog.askdirectory()
os.chdir(dir)
for i in os.listdir(dir):
    if i.endswith(".mp3"):
        songs.append(i)

print songs
pygame.mixer.init()
pygame.mixer.music.load(songs[0])


def play():
    pygame.mixer.music.play()
    trkname=songs[trkno]
    
def stop():
    pygame.mixer.music.stop()
    trkname=songs[trkno]

def nexttrk():
    global trkno
    trkno+=1
    pygame.mixer.music.load(songs[trkno])
    pygame.mixer.music.play()
    trkname=songs[trkno]

def prevtrk():
    global trkno
    global trkname
    trkno-=1
    pygame.mixer.music.load(songs[trkno])
    pygame.mixer.music.play()
    trkname=songs[trkno]

font1='Courier', 25, 'bold'
trkname=StringVar()
trkname="AB369Player"
Button(master,text='>>',command=nexttrk).grid(row=1,column=3,sticky=W,pady=4)
Button(master,text='<<',command=prevtrk).grid(row=1,column=0,sticky=W,pady=4)
Button(master,text='||',command=stop).grid(row=1,column=1,sticky=W,pady=4)
Button(master,text='>',command=play).grid(row=1,column=2,sticky=W,pady=4)
Label(master,text=trkname,font=font1).grid(row=1,column=4)


mainloop()
