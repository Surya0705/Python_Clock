from tkinter import Tk # Importing the tkinter module.
from tkinter import Label # Importing the tkinter module.
import time # Importing the time module for our Clock's time.
import sys # Importing the sys module.

Root = Tk() # Defining the root.
Root.title("Python Clock") # Giving the title to our tkinter window.
Root.resizable(0, 0) # Disabled resizing the Window so it doesn't appear messed if resized.

def Time(): # Defining the Time function.
    Time_Var = time.strftime("%I:%M:%S %p") # Giving it a display format.
    Clock.config(text=Time_Var) # Configuration.
    Clock.after(200, Time) # Refreshing time every 200 miliseconds to get latest time.

Clock = Label(Root, font=("Britannic Bold", 100), background="black", foreground="cyan")

Clock. pack() # For running.
Time() # For running.
Root.mainloop() # For running.