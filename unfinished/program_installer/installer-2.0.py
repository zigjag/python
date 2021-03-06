from tkinter import ttk
from tkinter import Tk, Menu
from tkinter import *
import json
import os

with open('repos.json', 'r') as fr:
    repoDict = json.load(fr)

class App(Tk):
    global gitList
    def __init__(self):
        super(App, self).__init__()
        self.title('Installer Gui')
        self.geometry("800x480")
        self.create_menus()

        notebook = ttk.Notebook(self)
        notebook.pack(fill='both', expand=True)
        tab1 = ttk.Frame(notebook)
        self.create_requirements(tab1)
        tab2 = ttk.Frame(notebook)
        tab3 = ttk.Frame(notebook)
        notebook.add(tab1, text='Required')
        notebook.add(tab2, text='Github Programs')
        notebook.add(tab3, text='Help')
        notebook.select(1)

        self.create_buttons(tab2)

    def create_menus(self):# TODO: Finish this
        menubar = Menu(self)
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=file_menu)
        self.config(menu=menubar)

    def create_requirements(self, parent):
        import platform
        Label(parent, text='Operating System: ').grid(row=0, column=0, sticky='w')
        os_system = platform.platform()
        os_label = Label(parent, text=os_system)
        os_label.grid(row=0, column=1, sticky='w')

        Label(parent, text='Python Version').grid(row=1, column=0, sticky='w')
        python_version = platform.python_version()
        py_label = Label(parent, text=python_version)
        py_label.grid(row=1, column=1, sticky='w')

    def create_buttons(self, parent, button_text='Click Here', command=None):
        frame1 = ttk.Frame(parent)
        frame1.pack()
        all_button = ttk.Button(frame1, text='Install All')
        all_button.pack(side='top', anchor='nw')

        frame2 = ttk.Frame(parent)
        frame2.pack()

        column = 0
        row = 0
        for v in repoDict['repos'].values():
            label = ttk.Label(frame2, text=v +' repo' + ':')
            label.grid(row=row, column=column, sticky='e', padx=10)

            repo_cmd = f'git clone https://github.com/zigjag/{v}.git'

            button = ttk.Button(frame2, text=button_text, command=lambda: os.system(repo_cmd))# TODO
            button.grid(row=row, column=column+1, pady=5)
            row += 1
            if row % 10 == 0:
                row = 0
                column += 2

        def all():
            for frame in frame2.winfo_children():
                if 'button' in str(frame):
                    frame.invoke()

        all_button.config(command=all)

    def system_command(self, command):# TODO
        os.system(command)

if __name__ == '__main__':

    app = App()
    app.mainloop()
