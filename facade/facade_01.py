import tkinter as tk

from facade.data_to_display import circle_show, square_show
from facade.view_1 import view1, view2

# Design Patterns - Structural pattern - Facade


class facade_1:
    def __init__(self, root):
        self.root = root

    def open_view(self):
        frm = tk.Frame(self.root)

        def comm1():
            v1 = view1(frm, circle_show).open_view1()
            v1.grid(row=0, column=1)

        btn1 = tk.Button(frm, text='View 1', command=comm1)
        btn1.grid(row=0, column=0, sticky='n')

        def comm2():
            v1 = view2(frm, square_show).open_view2()
            v1.grid(row=0, column=1)
        btn2 = tk.Button(frm, text='View 2', command=comm2)
        btn2.grid(row=1, column=0, sticky='n')

        frm.grid(row=0, column=0)

def main():
    app = tk.Tk()
    fac = facade_1(app).open_view()
    app.mainloop()

if __name__ == '__main__':
    main()