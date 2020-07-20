from tkinter import *
from pytube import YouTube
def download():
    link=e.get()
    yt=YouTube(link)
    video=yt.streams[0].download()
    l1.configure(text="downloaded successfully")
    print(video)
root=Tk()
root.geometry("400x400")
root.title("Video Download")
Label(root, text="Download App",font="algerian 20 bold").pack()
e=Entry(root,text="enter the url")
e.pack()
b=Button(root,text="download",command=download)
b.pack()

l1=Label(root)
l1.pack()
