import tkinter as tk # Importing text as tk
from tkinter import ttk # Importing text as ttk
from tkinter import messagebox # Adding a message box 
import json # Saving data in json file

# Naming my window as tk
window = tk.Tk()

# The Title of the window
window.title("Julie’s Party Hire")

# Geometry of the window
window.geometry("700x700")

# Defining the Maximun and the minimun size of the window sto its locked and unchanged, (width,hieght)
window.minsize(700, 700)
window.maxsize(700, 700)

# giving the window a background colour
window.config(bg="#FFF1DC")

# Defining Constants
Max_num_of_items = 500
Min_num_of_items = 1

# Define the data structure to store items information
items_data = {}

# Create a line and draw it on the canvas
my_rect = tk.Canvas(window, width=800, height=20)
my_rect.pack()
