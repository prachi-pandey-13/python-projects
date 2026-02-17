import tkinter as tk
import time
from PIL import Image, ImageTk

# Main Application Window
root = tk.Tk()
root.title("Image Slideshow Album")
root.geometry("900x900")

# List of Image Paths
image_paths = [
    r"C:\Users\prach\OneDrive\Pictures\Saved Pictures\ChatGPT Image Aug 3, 2025, 09_07_29 PM.png",
    r"C:\Users\prach\OneDrive\Pictures\Saved Pictures\download.jpg"
]

image_size = (700, 700)
image = []
for path in image_paths:
    img = Image.open(path)
    img = img.resize(image_size)
    image.append(img) # Adding each image in list

# Convert PIL images to Tkinter compatible image
final_images = []
for img in image:
    photo = ImageTk.PhotoImage(img)
    final_images.append(photo)

# Label widget to keep photo
image_label = tk.Label(root)
image_label.pack(pady=30)

# Slideshow Function
def start_slideshow():
    for photo in final_images:
        image_label.config(image=photo)
        image_label.image = photo
        root.update()
        time.sleep(2)

# Button
play_button = tk.Button(
    root,
    text= "Play the slideshow",
    font=("Arial",17),
    command=start_slideshow
)
play_button.pack(pady=40)
root.mainloop()

