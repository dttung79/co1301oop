from tkinter import filedialog
from client import Client
from gui_base import MyWindow
from tkinter import *
from tkinter import messagebox as msb

class AddClientGUI(MyWindow):
    def __init__(self, title='Add Client Form', dimensions='600x400'):
        super().__init__(title, dimensions)
        self.clients = []

    def create_widgets(self):
        self.lbl_clients = Label(self.window, text='All Clients')
        self.lbl_clients.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        self.lbl_enter = Label(self.window, text='Enter Client Details')
        self.lbl_enter.grid(row=0, column=1, columnspan=3, sticky=W, padx=5, pady=5)

        self.lst_clients = Listbox(self.window, width=30, height=10, selectmode=SINGLE, exportselection=0)
        self.lst_clients.grid(row=1, column=0, rowspan=5, padx=5, pady=5)
        self.lst_clients.bind('<<ListboxSelect>>', self.lst_clients_select)

        self.lbl_name = Label(self.window, text='Name')
        self.lbl_name.grid(row=1, column=1, sticky=E, padx=5, pady=5)

        self.txt_name = Entry(self.window)
        self.txt_name.grid(row=1, column=2, columnspan=2, sticky=W, padx=5, pady=5)

        self.lbl_project = Label(self.window, text='Project')
        self.lbl_project.grid(row=2, column=1, sticky=E, padx=5, pady=5)

        self.txt_project = Entry(self.window)
        self.txt_project.grid(row=2, column=2, columnspan=2, sticky=W, padx=5, pady=5)

        self.lbl_budget = Label(self.window, text='Budget')
        self.lbl_budget.grid(row=3, column=1, sticky=E, padx=5, pady=5)

        self.txt_budget = Entry(self.window)
        self.txt_budget.grid(row=3, column=2, columnspan=2, sticky=W, padx=5, pady=5)

        self.lbl_vip = Label(self.window, text='VIP')
        self.lbl_vip.grid(row=4, column=1, sticky=E, padx=5, pady=5)

        self.vip = IntVar()
        self.rd_vip_yes = Radiobutton(self.window, text='Yes', variable=self.vip, value=1)
        self.rd_vip_yes.grid(row=4, column=2, sticky=W, padx=5, pady=5)

        self.rd_vip_no = Radiobutton(self.window, text='No', variable=self.vip, value=0)
        self.rd_vip_no.grid(row=4, column=3, sticky=E, padx=5, pady=5)

        self.btn_add = Button(self.window, text='Add Client', command=self.btn_add_click)
        self.btn_add.grid(row=5, column=1, columnspan=3, sticky=W+E, padx=5, pady=5)

        self.btn_save = Button(self.window, text='Save Clients', command=self.btn_save_click)
        self.btn_save.grid(row=6, column=0, padx=5, pady=5, sticky=W+E)

        self.btn_update = Button(self.window, text='Update Client', command=self.btn_update_click)
        self.btn_update.grid(row=6, column=1, columnspan=3, padx=5, pady=5, sticky=W+E)

        self.btn_load = Button(self.window, text='Load Clients', command=self.btn_load_click)
        self.btn_load.grid(row=7, column=0, padx=5, pady=5, sticky=W+E)

        self.btn_delete = Button(self.window, text='Delete Client', command=self.btn_delete_click)
        self.btn_delete.grid(row=7, column=1, columnspan=3, padx=5, pady=5, sticky=W+E)

    def btn_delete_click(self):
        try:
            # get selected index in the listbox
            sel_index = self.lst_clients.curselection()
            self.clients.pop(sel_index[0])
            self.lst_clients.delete(sel_index[0])
            msb.showinfo('Success', 'Client deleted successfully')
        except IndexError:
            msb.showerror('Error', 'Please select a client to delete.')
    
    def btn_update_click(self):
        try:
            # get selected index in the listbox
            sel_index = self.lst_clients.curselection()
            # get selected client
            sel_client = self.clients[sel_index[0]]
        except IndexError:
            msb.showerror('Error', 'Please select a client to update.')
            return
        
        # get new values
        name = self.txt_name.get()
        project = self.txt_project.get()
        budget = int(self.txt_budget.get())
        vip = self.vip.get() == 1
        # update client details
        sel_client.name = name
        sel_client.project = project
        sel_client.budget = budget
        sel_client.vip = vip
        # update listbox with new name
        self.lst_clients.delete(sel_index[0])
        self.lst_clients.insert(sel_index[0], name)
        msb.showinfo('Success', 'Client updated successfully')
    def btn_save_click(self):
        try:
            # open file dialog to save file
            file_name = filedialog.asksaveasfilename(filetypes=[('CSV Files', '*.csv')])
            with open(file_name, 'w') as file:
                # write header
                file.write('Name,Project,Budget,VIP\n')
                for client in self.clients:
                    file.write(f'{client.name},{client.project},{client.budget},{client.vip}\n')
            msb.showinfo('Success', 'Clients saved successfully')
        except FileNotFoundError:
            msb.showerror('Error', 'Please choose a file to save.')
        except Exception as e:
            msb.showerror('Error', str(e))
    
    def btn_load_click(self):
        # open file dialog to load file
        try:
            file_name = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
            with open(file_name, 'r') as file:
                # read header
                file.readline()
                for line in file:
                    row = line.strip().split(',')   # read a row and split it by comma
                    name = row[0]
                    project = row[1]
                    budget = int(row[2])
                    vip = row[3] == 'True'
                    # create a client object
                    client = Client(name, project, budget, vip)
                    self.clients.append(client)    # add client to the list of clients
                    self.lst_clients.insert(END, name)  # add client name to the listbox
            msb.showinfo('Success', 'Clients loaded successfully')
        except FileNotFoundError:
            msb.showerror('Error', 'Please choose a file to load.')
        except Exception as e:
            msb.showerror('Error', 'Not a valid file format or content.')

    def btn_add_click(self):
        try:
            # get name
            name = self.txt_name.get()
            # get project
            project = self.txt_project.get()
            # get budget
            budget = int(self.txt_budget.get())
            # get vip
            vip = self.vip.get() == 1
            # create a client object
            client = Client(name, project, budget, vip)
            # add client name to the listbox
            self.lst_clients.insert(END, name)
            # add client to the list of clients
            self.clients.append(client)
        except ValueError as e:
            msb.showerror('Error', str(e))
            return

    def lst_clients_select(self, event):
        # get selected index
        sel_index = self.lst_clients.curselection()
        # get selected client
        sel_client = self.clients[sel_index[0]]
        # display selected client details
        self.txt_name.delete(0, END)
        self.txt_name.insert(0, sel_client.name)
        self.txt_project.delete(0, END)
        self.txt_project.insert(0, sel_client.project)
        self.txt_budget.delete(0, END)
        self.txt_budget.insert(0, sel_client.budget)
        if sel_client.vip:
            self.vip.set(1)
        else:
            self.vip.set(0)
if __name__ == '__main__':
    add_client = AddClientGUI()
    add_client.run()