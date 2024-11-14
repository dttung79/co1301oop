from tkinter import *
from tkinter import messagebox as msg

class MyWindow:
    def __init__(self, title='My Window', dimensions='600x400'):
        self.window = Tk()               # Create a window whic is an instance of Tk class
        self.window.title(title) # Set the title of the window
        self.window.geometry(dimensions)  # Set the size of the window

        self.create_widgets()            # Call the create_widgets method
    
    def create_widgets(self):
        pass

    def run(self):
        self.window.mainloop()           # Run the main event loop of the window