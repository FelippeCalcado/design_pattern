import tkinter as tk

class view1:
    def __init__(self, root, to_display=None):
        self.root = root
        self.to_display = to_display

    def open_view1(self):
        frm = tk.Frame(self.root)
        cvs = tk.Canvas(frm, bg='red', width=200, height=200)

        def cvs_txt():
            frm.destroy()
        btn_1 = tk.Button(frm, command=cvs_txt, text='Close')

        if self.to_display == None:
            pass
        else:
            self.to_display(cvs).image()
        cvs.grid(row=0, column=0)
        btn_1.grid(row=1, column=0, sticky='we')

        return frm

class view2:
    def __init__(self, root, to_display=None):
        self.root = root
        self.to_display = to_display

    def open_view2(self):
        frm = tk.Frame(self.root)
        cvs = tk.Canvas(frm, bg='blue', width=200, height=200)

        def cvs_txt():
            frm.destroy()
        btn_1 = tk.Button(frm, command=cvs_txt, text='Close')

        if self.to_display == None:
            pass
        else:
            self.to_display(cvs).image()

        cvs.grid(row=0, column=0)
        btn_1.grid(row=1, column=0, sticky='we')

        return frm


