import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
canvas.create_rectangle(10, 10, 100, 100, fill='red')
root.mainloop()
