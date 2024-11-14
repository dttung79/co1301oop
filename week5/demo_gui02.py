from tkinter import *
from tkinter import messagebox as msg

class MyWindow:
    def __init__(self):
        self.window = Tk()               # Create a window whic is an instance of Tk class
        self.window.title("Demo GUI 02") # Set the title of the window
        self.window.geometry("600x400")  # Set the size of the window

        self.create_widgets()            # Call the create_widgets method
    
    def create_widgets(self):
        self.lbl_hello = Label(self.window, text="Hello World!")
        self.lbl_hello.grid(row=0, column=0)

        self.btn_translate = Button(self.window, text="Translate", command=self.btn_translate_click)
        self.btn_translate.grid(row=0, column=1)

        self.txt_input = Entry(self.window)
        self.txt_input.grid(row=1, column=0)

        self.btn_hello = Button(self.window, text="Say Hello", command=self.btn_hello_click)
        self.btn_hello.grid(row=1, column=1)

        self.txt_output = Entry(self.window)
        self.txt_output.grid(row=2, column=0)

    def btn_translate_click(self):
        self.lbl_hello.config(text='Xin chào thế giới!')

    def btn_hello_click(self):
        name = self.txt_input.get() # Get the text from the input box
        hello = self.lbl_hello.cget("text") # Get the text from the label
        
        self.txt_output.delete(0, END)                  # clear current text in textbox
        self.txt_output.insert(0, f"{hello} {name}")    # insert new text into textbox

    def run(self):
        self.window.mainloop()           # Run the main event loop of the window

if __name__ == "__main__":
    my_window = MyWindow()             # Create an instance of MyWindow class
    my_window.run()                    # Run the window