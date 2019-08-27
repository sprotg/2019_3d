import tkinter as tk



class Min_gui(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.build_GUI()

    def change(self):
        self.lblName.config(text = 'Her står der noget nyt tekst.')


    def build_GUI(self):
        self.pack(side = tk.BOTTOM)
        self.lblName = tk.Label(self, text = 'her står laaaaaangt noget tekst i en label')
        self.butChange = tk.Button(self, text = 'Lav teksten om', command = self.change)
        self.lblName.pack(side = tk.LEFT)
        self.butChange.pack(side = tk.LEFT)

app = Min_gui()

app.mainloop()
