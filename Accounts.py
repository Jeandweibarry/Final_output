import tkinter as tk
import sqlite3

root = tk.Tk()

class GUI:
    def __init__(self):
        self.content_frame = tk.Frame(bg="gray")
        self.content_frame.pack(fill="both", expand=True)
    def frame(self):
        self.main_frame = tk.Frame(bg="gray", relief="raised", borderwidth=10, width=500, height=1080)
        self.main_frame.place(y=0, x=0)
    def canvas(self):
        self.canvas_content = tk.Canvas()

GUI = GUI()
GUI.frame()
root.attributes("-fullscreen", True)
root.mainloop()
