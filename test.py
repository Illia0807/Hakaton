import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk  # For working with images

# Importing functions for generating a fairy tale and working with the database
from story_api_request import generate_bedtime_story
from database import StoryDatabase

# Function for generating a fairy tale and opening a new window
def generate_story():
    # Retrieving data from input fields
    name = name_entry.get()
    character = character_var.get()
    location = location_var.get()
    
    # Generating a fairy tale using the generate_bedtime_story function
    story = generate_bedtime_story(name, character, location)

    # Opening a new window to display the fairy tale
    story_window = tk.Toplevel(root)
    story_window.title("Your fairy tale")
    story_window.geometry("600x400")

    # Creating a text field to display the fairy tale
    story_textbox = tk.Text(story_window, font=("Segoe Print", 12), wrap="word", height=10, width=50, bg="#000033", fg="white")
    story_textbox.insert(tk.END, story)
    story_textbox.config(state=tk.DISABLED) 
    story_textbox.pack(padx=20, pady=20)

    # Saving the fairy tale to the database
    db = StoryDatabase()
    db.save_story(name, character, location, story)
    db.close()



# Creating the main window
root = tk.Tk()
root.title("Your fairy tale")
root.geometry("600x400")

# Loading the background
bg_image = Image.open("stars.jpg")  
bg_image = bg_image.resize((600, 400), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  # Background covering the entire screen

# Centering elements
center_x = 200  
center_y = 50   
# Input field for entering a name
name_label = tk.Label(root, text="Enter your name:", font=("Lucida Calligraphy", 12, "italic"), bg="#000033", fg="white")
name_label.place(x=center_x, y=center_y)

name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.place(x=center_x, y=center_y + 30, width=200)

# Character selection
character_label = tk.Label(root, text="Choose a character:", font=("Arial", 12), bg="#000033", fg="white")
character_label.place(x=center_x, y=center_y + 70)

character_var = tk.StringVar()
character_combobox = ttk.Combobox(root, textvariable=character_var, values=["Wise Dragon", "Brave Knight", "Mysterious Mage"])
character_combobox.place(x=center_x, y=center_y + 100, width=200)
character_combobox.current(0)

# Location selection
location_label = tk.Label(root, text="Choose a location:", font=("Arial", 12), bg="#000033", fg="white")
location_label.place(x=center_x, y=center_y + 140)

location_var = tk.StringVar()
location_combobox = ttk.Combobox(root, textvariable=location_var, values=["Abandoned Castle", "Enchanted Forest", "Misty Mountains"])
location_combobox.place(x=center_x, y=center_y + 170, width=200)
location_combobox.current(0)

# Button for creating a fairy tale
generate_button = tk.Button(root, text="Create a fairy tale", font=("Arial", 12), bg="#ffcc00", command=generate_story)
generate_button.place(x=center_x + 50, y=center_y + 220)

root.mainloop()
