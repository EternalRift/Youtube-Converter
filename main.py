import tkinter as tk 
import os 
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube


# Main Window config 
Main_Window = tk.Tk()
Main_Window.title("Youtube Video Downloader")
Main_Window.geometry("628x437")
Main_Window.maxsize(628, 437)
Main_Window.minsize(628, 437)
icon = PhotoImage(file='Source/Assets/img/icon.png')
Main_Window.iconphoto(False,icon)

# About config
about_window = tk.Tk()
about_window.title("About")
about_window.geometry("628x437")
about_window.maxsize(628, 437)
about_window.minsize(628, 437)
about_window.withdraw()
icon_about = PhotoImage(file='Source/Assets/img/icon.png ')

#main window frames
convert_settings = Frame(Main_Window,bg="lightgray",height=120, width=585)

#convert var chk 
conv_var = IntVar()

#input field strings
file_path_var = StringVar()
url_path_var = StringVar()

def about_button():
    Main_Window.withdraw()
    messagebox.showinfo("penis","switch window is working dipshit")
    about_window.deiconify()

def file_explore():
    file_loc = filedialog.askdirectory(
        title="Select Where To Save File",
        initialdir="%USERPROFILE/Downloads"
    )
    file_path_var.set(file_loc)

def mp3_convert():
    url = url_path_var.get()
    path = file_path_var.get()
    video = YouTube(url)
    stream = video.streams.filter(only_audio=True).first()
    stream.download(path,filename=f"{video.author} {video.title}.mp3")
    messagebox.showinfo("Complete","Video has been converted and saved in : "+path)

def mp4_convert():
   url = url_path_var.get()
   path = file_path_var.get()
   video = YouTube(url)
   stream = video.streams.filter(res="720p").first()
   stream.download(path,filename=f"{video.author} {video.title}.mp4")
   messagebox.showinfo("Complete","Video has been converted and saved in : "+path)
    
def convert():
   n = conv_var.get()
   if n == 1:
       mp3_convert()
   elif n == 2:
    mp4_convert()

#buttons 
convert_button = Button(convert_settings,
                        text="Convert Video",
                        height=4,
                        width=20,
                        command=convert
                        
                         )
about_button_tk = Button(Main_Window,
                      text="About",
                      command=about_button)

browse_button = Button(Main_Window,
                       text="Browse",
                       command=file_explore,
                       height=1,
                       width=10
                       )

mp4_radio = Radiobutton(convert_settings,
                        text="Mp4",
                        variable=conv_var,
                        value=2,
                        height=2,
                        width=10,
                        bg="lightgray")

mp3_radio = Radiobutton(convert_settings,
                        text="Mp3",
                        variable=conv_var,
                        value=1,
                        height=2,
                        width=10,
                        bg="lightgray")
filetype_select_label = Label(convert_settings,
                              text="Select File Format to use:")
#input fields
path_input = Entry(Main_Window,
                   textvariable=file_path_var,
                   font=('calibre',10, 'bold'),
                   width=50
                   )
path_label = Label(Main_Window,text="Path to save file:",
                   font=('calibre',10, 'bold'))
url_input = Entry(Main_Window,
                  textvariable=url_path_var,
                  font=('calibre',10, 'bold'),
                  width=50
                  )
url_label = Label(Main_Window,
                  text="Input Youtube Link:",
                  font=('calibre',10, 'bold'))
                
#Button placement
convert_button.place(x=420,y=15) # inside frame x y diff
about_button_tk.place(x=20,y=400)
convert_settings.place(x=20,y=250)
mp3_radio.place(x=10, y=15)
mp4_radio.place(x=10,y=50)
# input field placement 
path_input.place(x=150,y=180)
path_label.place(x=10,y=180)
browse_button.place(x=535,y=180)
url_input.place(x=150,y=125)
url_label.place(x=10,y=125)

#GUI Loop KEEP AT BOTTM
mainloop()