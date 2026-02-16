# import tkinter module for creating GUI apps
import tkinter as tk
from tkinter import filedialog, messagebox

# main window code
root = tk.Tk()
# set window title
root.title("PRACHI'S TEXT EDITOR")
# set window size
root.geometry("800x600")

# create text area
text = tk.Text(
    root,
    wrap= tk.WORD, # wrap by words
    font = ("Helvetica",12)
)

text.pack(expand=True,fill=tk.BOTH)

# Main logic starts now
# Function-1 To create new file
def new_file():
    text.delete(1.0,tk.END)

# Function-2 To open a new file
def open_file():
    # open file dialogue
    file_path = filedialog.askopenfile(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        # open selected file
        with open(file_path, "r") as file:
            text.delete(1.0,tk.END)
            text.insert(tk.END, file.read())

# Function-3 Save the file
def save_file():
    # open save file dialog
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        with open(file_path,"w") as file:
            file.write(text.get(1.0,tk.END))
    messagebox.showinfo("Info", "File Saved Successfully.")

# Menu 
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
# New, Open, Save, Exit

# Add filemenu to menubar
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)



root.mainloop() # it starts and keep the window open
