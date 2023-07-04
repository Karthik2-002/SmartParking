from tkinter import Tk, Canvas, Frame, BOTH
from tkinter.ttk import Button, Style
from PIL import ImageTk, Image
import os

window = Tk()
window.title("Car Parking Slot Finder")
window.state("zoomed")
window.iconbitmap("./cps.ico")

# Create a custom style for the button
style = Style()
style.configure("TButton",
                foreground="blue",
                background="blue",
                font=("Helvetica", 25),
                relief="flat",
                padding=(50, 20))

canvas = Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight(), bg="white")
canvas.pack(fill=BOTH, expand=True)

bg_image = Image.open("car.png")
resized_image = bg_image.resize((window.winfo_screenwidth(), window.winfo_screenheight()))
bg = ImageTk.PhotoImage(resized_image)

canvas.create_image(0, 0, image=bg, anchor='nw')

def resize_image(e):
    global bg, resized_image
    resized_image = bg_image.resize((e.width, e.height))
    bg = ImageTk.PhotoImage(resized_image)
    canvas.itemconfig(background, image=bg)

    # Adjust the canvas size
    canvas.config(width=e.width, height=e.height)

    # Reposition the background image at the center
    canvas.coords(background, e.width // 2, e.height // 2)

window.bind("<Configure>", resize_image)

def check_slots():
    # Code to check slots goes here
    print("Slots checked!")
    os.system("python main.py")

button_frame = Frame(window)
button_frame.pack(pady=(0, 50))  # Added pady to create spacing at the bottom

check_button = Button(button_frame, text="Check Slots", command=check_slots, style="TButton")
check_button.pack()


button_frame.place(relx=0.23, rely=0.7, anchor="w")

# Position the background image in the center
background = canvas.create_image(window.winfo_screenwidth() // 2, window.winfo_screenheight() // 2, image=bg)

window.mainloop()
