import tkinter as tk

LARGE_FONT = ("Arial", 12)


class MultiWindowOODemo(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        main = tk.Toplevel(self)
        label = tk.Label(main, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(main, text="Visit Page 1",
                           command=lambda: self.show_window(PageOne, self))
        button.pack()

        button2 = tk.Button(main, text="Visit Page 2",
                            command=lambda: self.show_window(PageTwo, self))
        button2.pack()

        P1 = PageOne(self)
        P1.withdraw()
        P2 = PageTwo(self)
        P2.withdraw()
        main.

    def show_window(show, hide):
        hide.withdraw()
        show.deiconify()


class PageOne(tk.Toplevel):

    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: parent.show_window(parent, self))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: parent.show_window(PageTwo, self))
        button2.pack()


class PageTwo(tk.Toplevel):

    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: parent.show_window(parent, self))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: parent.show_window(PageOne, self))
        button2.pack()


app = MultiWindowOODemo()
app.mainloop()
