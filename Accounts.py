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
        self.accounts = tk.Frame(self.content_frame, bg="gray", relief="raised", borderwidth=10)
        self.accounts.pack(side="right")

    def canvas(self):
        self.canvas = tk.Canvas(self.accounts, width=1380, height=1080)
        self.canvas.pack(side="left", fill="y")

        self.scrollbar = tk.Scrollbar(self.accounts, command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame_container = tk.Frame(self.canvas)

        self.frame1 = tk.Frame(self.frame_container, width=1385, height=2500, bg='gray')
        self.frame1.pack()

        self.frame_container.update_idletasks()
        self.canvas.create_window(0, 0, window=self.frame_container, anchor='nw')
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        return self.frame1

    def account_display(self, text):
        self.account_frame = tk.Frame(self.frame1, height=500, width=1375)
        self.account_frame.pack()
        self.user_name = tk.Label(self.account_frame, font=("arial", 12, "bold"), text=text)
        self.user_name.place(x=50, y=50)



GUI = GUI()
GUI.frame()
GUI.canvas()
root.attributes("-fullscreen", True)
root.mainloop()
