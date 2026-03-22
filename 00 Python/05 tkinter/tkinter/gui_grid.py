import tkinter as tk

root = tk.Tk()

for x in range(3):
    root.grid_rowconfigure(x, weight=1)
    root.grid_columnconfigure(x, weight=1)

root.geometry("800x600")

label = tk.Label(root, text="Down right", bg="blue") #bg = background colour
label.grid(row=2, column=2)

root.mainloop()