from tkinter import *
from tkinter import messagebox as msg
from gui_base import MyWindow

class DemoRadioWindow(MyWindow):
    def __init__(self, title='Demo Radio Button', dimensions='400x200'):
        super().__init__(title, dimensions)

    def create_widgets(self):
        self.choice_var = StringVar()
        self.rd_python = Radiobutton(self.window, text='Python', 
                                     variable=self.choice_var, value='Python', 
                                     command=self.rd_selected)
        self.rd_python.grid(row=0, column=0, sticky=W)

        self.rd_java = Radiobutton(self.window, text='Java', 
                                   variable=self.choice_var, value='Java',
                                   command=self.rd_selected)
        self.rd_java.grid(row=1, column=0, sticky=W)

        self.rd_csharp = Radiobutton(self.window, text='C#',
                                        variable=self.choice_var, value='C#',
                                        command=self.rd_selected)
        self.rd_csharp.grid(row=2, column=0, sticky=W)

        # set default choice
        self.choice_var.set('Python')

        self.lbl_language = Label(self.window, text='You selected: Python, Level: Easy')
        self.lbl_language.grid(row=3, column=0, sticky=W)

        self.level_var = StringVar()
        self.rd_easy = Radiobutton(self.window, text='Easy', 
                                   variable=self.level_var, value='Easy',
                                   command=self.rd_selected)
        self.rd_easy.grid(row=0, column=1, sticky=W)
    
    def rd_selected(self):
        selected = self.choice_var.get()    # get the selected value from radio buttons
        # update the label
        self.lbl_language.config(text=f'You selected: {selected}')

if __name__ == '__main__':
    window = DemoRadioWindow()
    window.run()