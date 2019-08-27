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
        self.lblName = tk.Label(self, text = 'her står laaaaaangt noget tekst i en label')
        self.butChange = tk.Button(self, text = 'Lav teksten om', command = self.change)
        self.enText = tk.Entry(self, text = '')
        self.butChange.pack(side = tk.TOP)
        self.lblName.pack(side = tk.TOP)
        self.enText.pack(side = tk.TOP)

app = Min_gui()

app.mainloop()
