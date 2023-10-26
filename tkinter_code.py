import tkinter as tk
from tkinter import ttk, messagebox
import json

# Naming my window as tk
window = tk.Tk()

# The Title of the window
window.title("Julie’s Party Hire")

# Geometry of the window
window.geometry("640x600")

# Defining the Maximum and the minimum size of the window to keep it locked and unchanged (width, height)
window.minsize(640, 600)
window.maxsize(640, 600)

# giving the window a background color
window.config(bg="grey")

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
    entry = tk.Entry(window, border=2, relief="solid", fg="#929090")
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

# delete Button
delete_button = tk.Button(
    window, text="Delete Row", bg="#FF914D", fg="black", command=lambda: delete_data())
delete_button.place(x=560, y=130)

# Exitprogram Button
Exitprogram = tk.Button(
    window, text="Exit Program", bg="red", fg="black", command=exit)
Exitprogram.place(x=550, y=170)

# Function to handle submit button


# Counter for generating unique IDs
id_counter = 1

# Function to handle submit button


def submit_data():
    global id_counter

    # Retrieve data from entry boxes
    full_name = name_entry.get()    
    receipt_number = receipt_entry.get()
    item_hired = item_entry.get()
    num_items = num_item_entry.get()

    # Check if all fields are filled
    if not all([full_name, receipt_number, item_hired, num_items]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Add data to Treeview
    trv.insert("", "end", values=(id_counter, full_name,
               receipt_number, item_hired, num_items))

    # Add data to items_data dictionary
    items_data[id_counter] = {
        "Full Name": full_name,
        "Receipt Number": receipt_number,
        "Item Hired": item_hired,
        "Number of Items Hired": num_items
    }

    # Increment the ID counter
    id_counter += 1

    # Clear entry boxes
    name_entry.delete(0, tk.END)
    receipt_entry.delete(0, tk.END)
    item_entry.delete(0, tk.END)
    num_item_entry.delete(0, tk.END)

# Function to handle update button


def update_data():
    # Get the selected item from Treeview
    selected_item = trv.selection()

    if not selected_item:
        messagebox.showerror("Error", "Please select a row to update.")
        return

    # Get the values of the selected item
    values = trv.item(selected_item, 'values')

    # Fill entry boxes with the selected values
    name_entry.delete(0, tk.END)
    name_entry.insert(0, values[1])  # Full Name
    receipt_entry.delete(0, tk.END)
    receipt_entry.insert(0, values[2])  # Receipt Number
    item_entry.delete(0, tk.END)
    item_entry.insert(0, values[3])  # Item Hired
    num_item_entry.delete(0, tk.END)
    num_item_entry.insert(0, values[4])  # Number of Items Hired

    # Remove the selected item from Treeview
    trv.delete(selected_item)

def delete_data():
    # Get the selected item from Treeview
    selected_item = trv.selection()

    if not selected_item:
        messagebox.showerror("Error", "Please select a row to delete.")
        return

    # Remove the selected item from Treeview
    trv.delete(selected_item)


#                      <-------Treeview Box -------->
# Create the Treeview with striped lines
trv = ttk.Treeview(window, columns=(1, 2, 3, 4, 5),
                   show="headings", height=50, style="mystyle.Treeview")
trv.place(x=0, y=200)


# Input text in the heading
trv.heading(1, text="ID", anchor="center")  # Treeview Heading of ID
# Treeview Heading of Full Name
trv.heading(2, text="Full Name", anchor="center")
# Treeview Heading of Receipt Number2
trv.heading(3, text="Receipt Number", anchor="center")
# Treeview Heading of Item Hired
trv.heading(4, text="Item Hired", anchor="center")
# Treeview Heading of Number of Items Hired
trv.heading(5, text="Number of Items Hired", anchor="center")

# Labeling Treeview Heading in a column for ID
trv.column("#1", anchor="w", width=40, stretch=True)
# Labeling Treeview Heading in a column for Name
trv.column("#2", anchor="w", width=150, stretch=False)
# Labeling Treeview Heading in a column for Receipt Number
trv.column("#3", anchor="w", width=150, stretch=False)
# Labeling Treeview Heading in a column for Item Hired
trv.column("#4", anchor="w", width=150, stretch=False)
# Labeling Treeview Heading in a column for Number of items hired
trv.column("#5", anchor="w", width=150, stretch=False)


window.mainloop()
