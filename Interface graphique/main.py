import tkinter as tk
from tkinter import ttk

fenetre = tk.Tk()
fenetre.title("Ma premiere fenetre")
fenetre.geometry("400x300")

fenetre.mainloop()

label = ttk.Label(fenetre, text="Hello world")
label.pack(pady=20)
