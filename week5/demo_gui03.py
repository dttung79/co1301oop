from tkinter import *
from tkinter import messagebox as msg

class MyWindow:
    def __init__(self):
        self.window = Tk()               # Create a window whic is an instance of Tk class
        self.window.title("Demo GUI 03") # Set the title of the window
        self.window.geometry("600x400")  # Set the size of the window

        self.create_widgets()            # Call the create_widgets method
    
    def create_widgets(self):
        self.lbl_product = Label(self.window, text="Product:")
        self.lbl_product.grid(row=0, column=0)

        self.txt_product = Entry(self.window)
        self.txt_product.grid(row=0, column=1)

        self.lbl_price = Label(self.window, text="Price:")
        self.lbl_price.grid(row=1, column=0)

        self.txt_price = Entry(self.window)
        self.txt_price.grid(row=1, column=1)

        self.lbl_quantity = Label(self.window, text="Quantity:")
        self.lbl_quantity.grid(row=2, column=0)

        self.txt_quantity = Entry(self.window)
        self.txt_quantity.grid(row=2, column=1)

        self.btn_submit = Button(self.window, text="Submit", command=self.btn_submit_click)
        self.btn_submit.grid(row=3, column=1, sticky=W)

        self.lbl_total = Label(self.window, text="Total:")
        self.lbl_total.grid(row=4, column=0)

        self.total = StringVar()
        self.txt_total = Entry(self.window, textvariable=self.total)
        self.txt_total.grid(row=4, column=1)

    def btn_submit_click(self):
        price = int(self.txt_price.get())
        quantity = int(self.txt_quantity.get())
        self.total.set(price * quantity)

    def run(self):
        self.window.mainloop()           # Run the main event loop of the window


if __name__ == "__main__":
    my_window = MyWindow()             # Create an instance of MyWindow class
    my_window.run()                    # Run the window