from tkinter import *
from tkinter import messagebox as msg

class MyWindow:
    def __init__(self):
        self.window = Tk()               # Create a window whic is an instance of Tk class
        self.window.title("Demo GUI 01") # Set the title of the window
        self.window.geometry("600x400")  # Set the size of the window

        self.create_widgets()            # Call the create_widgets method

    def create_widgets(self):
        self.label = Label(self.window,         # specify the parent window
                           text="Hello World!") # specify the text of the label
        self.label.grid(row=0, column=0)

        self.button = Button(self.window, text="Click Me!", 
                             command=self.button_click) # bind the method to the button click event
        self.button.grid(row=1, column=0)
    
    # method that handles the button click event 
    def button_click(self):
        msg.showinfo("Message", "You clicked the button!")

    def run(self):
        self.window.mainloop()           # Run the main event loop of the window


if __name__ == "__main__":
    my_window = MyWindow()             # Create an instance of MyWindow class
    my_window.run()                    # Run the window