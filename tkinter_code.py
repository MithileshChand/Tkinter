import tkinter as tk
from tkinter import ttk, messagebox
import json

# Naming my window as tk
window = tk.Tk()

# The Title of the window
window.title("Julie’s Party Hire")

# Geometry of the window
window.geometry("500x600")

# Defining the Maximum and the minimum size of the window to keep it locked and unchanged (width, height)
window.minsize(500, 600)
window.maxsize(500, 600)

# giving the window a background color
window.config(bg="#FFF1DC")

# Defining Constants
Max_num_of_items = 500
Min_num_of_items = 1

# Define the data structure to store items information
items_data = {}

#                            <----Labels and Entry Boxes---->

# Function to set the font and position for labels


def create_label(text, row, column):
    label = tk.Label(window, text=text, background="#38B6FF",
                     font=("Arial", 10))
    label.grid(row=row, column=column, sticky="e", padx=10, pady=10)
    return label

# Function to create entry boxes


def create_entry(row, column):
    entry = tk.Entry(window, border=1, relief="solid", fg="#929090")
    entry.grid(row=row, column=column, sticky="w", padx=10, pady=10)
    return entry


# Label and Entry for Full Name
name_label = create_label("Full Name:", 0, 0)
name_entry = create_entry(0, 1)

# Label and Entry for Receipt Number
receipt_num_label = create_label("Receipt Number:", 1, 0)
receipt_entry = create_entry(1, 1)

# Label and Entry for Item Hired
item_label = create_label("Item Hired:", 2, 0)
item_entry = create_entry(2, 1)

# Label and Entry for Number of Items
num_item_label = create_label("Number of items:", 3, 0)
num_item_entry = create_entry(3, 1)

# Submit Button
submit_button = tk.Button(
    window, text="Submit", bg="green", fg="black", command=lambda: submit_data())
submit_button.place(x=320, y=90)

# Update Button
update_button = tk.Button(
    window, text="Update", bg="yellow", fg="black", command=lambda: update_data())
update_button.place(x=320, y=130)

# Function to handle submit button


def submit_data():
    # Add your logic to handle data submission
    pass

# Function to handle update button


def update_data():
    # Add your logic to handle data update
    pass


window.mainloop()
