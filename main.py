# Simple TkInter app
import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Python App')
    
        button = tk.Button(self, text="Click to flip the text", command=self.flipper)
        button.pack(padx=5, pady=5)   

        self.entry = tk.Entry(self, width=30)
        self.entry.insert(0, "Hello, my name is Flipper!") # default text
        self.entry.pack(padx=7, pady=7)

    def flipper(self):
        s = self.entry.get() # get current text
        self.entry.delete(0, 'end') # delete from char 0 to end
        self.entry.insert(0, s[::-1]) # insert flipped text

# make app object and run
app = Application()
app.mainloop()
