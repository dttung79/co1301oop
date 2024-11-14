from tkinter import *
from tkinter import messagebox as msg

class MyWindow:
    def __init__(self):
        self.window = Tk()               # Create a window whic is an instance of Tk class
        self.window.title("Demo GUI 01") # Set the title of the window
        self.window.geometry("600x400")  # Set the size of the window

        self.create_widgets()            # Call the create_widgets method

    def create_widgets(self):
        lbl_menu = Label(self.window, text="Menu")
        lbl_menu.grid(row=0, column=0)

        self.noodle_selected = BooleanVar()
        chk_noodle = Checkbutton(self.window, text="Noodle ($5)", 
                                 variable=self.noodle_selected, command=self.calculate_payment)
        chk_noodle.grid(row=1, column=1, sticky=W)

        self.banhmy_selected = BooleanVar()
        chk_banhmy = Checkbutton(self.window, text="Banh My ($3)", 
                                 variable=self.banhmy_selected, command=self.calculate_payment)
        chk_banhmy.grid(row=2, column=1, sticky=W)

        self.rice_selected = BooleanVar()
        chk_rice = Checkbutton(self.window, text="Fried Rice ($7)", 
                               variable=self.rice_selected, command=self.calculate_payment)
        chk_rice.grid(row=3, column=1, sticky=W)

        self.lbl_payment = Label(self.window, text="Payment: $0")
        self.lbl_payment.grid(row=4, column=0)

    def calculate_payment(self):
        total = 0
        if self.noodle_selected.get():
            total += 5
        if self.banhmy_selected.get():
            total += 3
        if self.rice_selected.get():
            total += 7
        self.lbl_payment.config(text="Payment: $" + str(total))
    
    def run(self):
        self.window.mainloop()           # Run the main event loop of the window


if __name__ == "__main__":
    my_window = MyWindow()             # Create an instance of MyWindow class
    my_window.run()                    # Run the window