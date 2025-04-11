import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk()
root.title("Изображение в Canvas")
image = Image.open('galgo.png')
photo = ImageTk.PhotoImage(image)
canvas = tk.Canvas(root, width=photo.width(), height=photo.height())
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=photo)
canvas.image = photo
root.mainloop()