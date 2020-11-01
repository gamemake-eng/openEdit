#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.geometry("700x600")
about = tk.Label(text="Open Edit - MIT License")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
text = tk.Text(root, height=h, width=w)
#saving files
def save():
      savefile = filedialog.asksaveasfilename(initialdir = "/home", title = "save as...", filetypes=(("plain text", "*.txt"),("python script", "*.py"),("javascript", "*.js"), ("godot script", "*.gd")))
      areatext = text.get("1.0", "end")
      open(savefile, "w").write(areatext)
#loading files
def load():
      filename = filedialog.askopenfilename(initialdir = "/home", title = "click a file")
      filetext = open(filename, "r")
      text.delete("1.0", "end")
      text.insert(tk.END, filetext.read())
      filetext.close()

save = tk.Button(root, text="save", command=save)
load = tk.Button(root, text="load", command=load)
#buttons
save.pack()
load.pack()
#about
about.pack()
#typing area
text.pack()
areatext = text.get("1.0", "end")
root.mainloop()