from tkinter import *
from tkinter import messagebox as msg

class MyWindow:
    def __init__(self):
        self.window = Tk()               # Create a window whic is an instance of Tk class
        self.window.title("Convert Text") # Set the title of the window
        self.window.geometry("600x400")  # Set the size of the window

        self.create_widgets()            # Call the create_widgets method
    
    def create_widgets(self):
        self.lbl_original = Label(self.window, text="Original Text")
        self.lbl_original.grid(row=0, column=0)

        self.lbl_convert = Label(self.window, text="Convert")
        self.lbl_convert.grid(row=0, column=1)

        self.lbl_output = Label(self.window, text="Converted Text")
        self.lbl_output.grid(row=0, column=2)

        self.txt_original = Entry(self.window)
        self.txt_original.grid(row=1, column=0)

        self.btn_title = Button(self.window, text="Title", width=15, command=self.btn_title_click)
        self.btn_title.grid(row=1, column=1)

        self.txt_convert = Entry(self.window)
        self.txt_convert.grid(row=1, column=2)

        self.btn_upper = Button(self.window, text="UPPER", width=15, command=self.btn_upper_click)
        self.btn_upper.grid(row=2, column=1)

        self.btn_lower = Button(self.window, text="lower", width=15, command=self.btn_lower_click)
        self.btn_lower.grid(row=3, column=1)

    def convert_text(self, converter):
        original = self.txt_original.get()
        convert = converter(original)
        self.txt_convert.delete(0, END)
        self.txt_convert.insert(0, convert)
    
    def btn_title_click(self):
        self.convert_text(lambda x: x.title())

    def btn_upper_click(self):
        self.convert_text(lambda x: x.upper())

    def btn_lower_click(self):
        self.convert_text(lambda x: x.lower())

    def run(self):
        self.window.mainloop()           # Run the main event loop of the window

if __name__ == "__main__":
    my_window = MyWindow()             # Create an instance of MyWindow class
    my_window.run()                    # Run the window