import tkinter as tk

class Min_gui(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.build_GUI()

    def change(self):
        t = self.enText.get()
        self.lblName.config(text = t)


    def build_GUI(self):
        self.pack(side = tk.BOTTOM)
        self.V = tk.Frame(self)
        self.H = tk.Frame(self)
        self.HT = tk.Frame(self.H)
        self.HB = tk.Frame(self.H)

        self.V.pack(side = tk.LEFT)
        self.H.pack(side = tk.RIGHT)
        self.HT.pack(side = tk.TOP)
        self.HB.pack(side = tk.BOTTOM)

        for i in range(4):
            b = tk.Button(self.V)
            b.pack(side = tk.TOP)
        for i in range(2):
            b = tk.Button(self.HT)
            b.pack(side = tk.LEFT)
        c = tk.Canvas(self.HB)


app = Min_gui()

app.mainloop()
