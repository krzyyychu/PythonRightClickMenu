import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()
messagebox.showinfo("Important info!", "Popup message!")

#Alternatively: 
#import tkinter.messagebox as box

# root = tkinter.Tk()

# root.title("Hello!")

# root.resizable(width="false", height="false")

# root.minsize(width=30, height=50)
# #root.maxsize(width=300, height=90)

# simple_label = tkinter.Label(root, text="Easy, right?")
# closing_button = tkinter.Button(root, text="Close window", command=root.destroy)

# simple_label.pack(fill="x")
# closing_button.pack(fill="x")

# root.mainloop()