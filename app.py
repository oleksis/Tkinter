import tkinter as tk
import random
import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def check_distance(event):
    button_coords = button.place_info()
    button_x = int(button_coords["x"]) + 25  # add half the button size (50 / 2)
    button_y = int(button_coords["y"]) + 25  # add half the button size (50 / 2)
    if (
        distance(button_x, button_y, event.x, event.y) < 100
    ):  # 100 is the distance threshold
        move_button()


def move_button():
    button.place(
        x=random.randint(0, window.winfo_width() - 50),
        y=random.randint(0, window.winfo_height() - 50),
    )


window = tk.Tk()
window.geometry("800x600")  # Set the size of the window to 800x600 pixels

button = tk.Button(window, text="Catch me!", width=10, height=2)
button.place(x=window.winfo_width() // 2, y=window.winfo_height() // 2)

window.bind("<Motion>", check_distance)


def main():
    window.mainloop()


if __name__ == "__main__":
    main()
