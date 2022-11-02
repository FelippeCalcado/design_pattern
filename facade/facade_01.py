import tkinter as tk

from facade.data_to_display import circle_show, square_show
from facade.view_1 import view1, view2

# Design Patterns - Structural pattern - Facade.


class Facade1:
    def __init__(self, root):
        self.root = root
        self.current_view = ''
        self.current_canvas = ''

    def open_view(self):
        frm = tk.Frame(self.root)

        def comm1():
            v1_base = view1(frm, circle_show)
            v1 = v1_base.open_view1()
            v1.grid(row=0, column=1, rowspan=2)
            try:
                self.current_view.destroy()
            except:
                pass
            self.current_view = v1
            self.current_canvas = v1_base.canvas
        btn1 = tk.Button(frm, text='View 1', command=comm1)
        btn1.grid(row=0, column=0, sticky='n')

        def comm2():
            v1_base = view2(frm, square_show)
            v1 = v1_base.open_view2()
            v1.grid(row=0, column=1, rowspan=2)
            try:
                self.current_view.destroy()
            except:
                pass
            self.current_view = v1
            self.current_canvas = v1_base.canvas

        btn2 = tk.Button(frm, text='View 2', command=comm2)
        btn2.grid(row=1, column=0, sticky='n')

        frm.grid(row=0, column=0, rowspan=2)
        frm.rowconfigure(0, weight=0)
        frm.rowconfigure(1, weight=1)


def main():
    app = tk.Tk()
    fac_base = Facade1(app)
    fac = fac_base.open_view()

    app.mainloop()


if __name__ == '__main__':
    main()
