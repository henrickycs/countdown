#make an countdown clock that makes noise when time runs out

import time
from tkinter import *
from tkinter import messagebox
from pygame import mixer

def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()
 
# Create object
root = Tk()

# Define the geometry of the window
root.geometry("400x300")
root.resizable(0,0)
root.attributes('-topmost', 0)

#define title
root.title("Timer")

# set background color
root.config(bg='#345')
  
# declaration of variables
minute=StringVar()
second=StringVar()
  
# setting the default value as 0
minute.set("00")
second.set("00")
  
# Using Entry class to take input from the user
  
mins_box = Entry(
	root, 
	width=3, 
	font=("Arial",18,""),
	textvariable=minute,
    justify=CENTER)

mins_box.place(x=150,y=120)
  
sec_box = Entry(
	root, 
	width=3, 
	font=("Arial",18,""),
	textvariable=second,
    justify=CENTER)

sec_box.place(x=210,y=120)
  
  
def countdowntimer():
    try:
        # store the user input
        user_input = int(minute.get())*60 + int(second.get())
    except:
        messagebox.showwarning('', 'Texto Inválido')
    while user_input >-1:
         
        # divmod(firstvalue = user_input//60, secondvalue = user_input%60)
        mins,secs = divmod(user_input,60)
  
        # store the value up to two decimal places
        # using the format() method
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
  
        # updating the GUI window 
        root.update()
        time.sleep(1)
  
        # if user_input value = 0, then a messagebox pop's up
        # with a message and a beep warning
        if(user_input == 0):
           mixer.init()
           #path of the sound
           recording = mixer.Sound(r"C:\Your\Path\For\Mp3\File\beep-06.mp3")
           #making a infinite loop
           recording.play(loops= -1)
           messagebox.showinfo("Aviso", "O tempo acabou!", icon = "info", parent = None)
           #the annoying sound stops after messagebox popup
           recording.stop()
        # decresing the value of temp 
        # after every one sec by one
        user_input -= 1
 
# button widget
btn = Button(root, text='Iniciar', bd='5',
             command= countdowntimer, width= 35)
btn.pack(side=BOTTOM)
center(root)
root.mainloop()