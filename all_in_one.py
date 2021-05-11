import tkinter as tk

LARGE_FONT = ("Verdana", 12)
root = tk.Tk()
container = tk.Frame(root)

container.pack(side="top", fill="both", expand=True)

container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

StartPage = tk.Frame(container)
PageOne = tk.Frame(container)
PageTwo = tk.Frame(container)
for F in (StartPage, PageOne, PageTwo):
    F.grid(row=0, column=0, sticky="nsew")


def show_frame(frame_to_raise):
    frame_to_raise.tkraise()


# Code for StartPaqe Content ####
sp_label = tk.Label(StartPage, text="Start Page", font=LARGE_FONT)
sp_label.grid(row=0, column=0, padx=5, pady=10)
sp_button = tk.Button(StartPage, text="Visit Page 1",
                      command=lambda: show_frame(PageOne))
sp_button.grid(row=1, column=0, padx=5, pady=10)
button2 = tk.Button(StartPage, text="Visit Page 2",
                    command=lambda: show_frame(PageTwo))
button2.grid(row=2, column=0, padx=5, pady=10)

# Code for PageOne Content ####
po_label = tk.Label(PageOne, text="Page One", font=LARGE_FONT)
po_label.grid(row=0, column=0, padx=5, pady=10)
po_button = tk.Button(PageOne, text="Back To Start",
                      command=lambda: show_frame(StartPage))
po_button.grid(row=1, column=0, padx=5, pady=10)
po_button2 = tk.Button(PageOne, text="Visit Page 2",
                       command=lambda: show_frame(PageTwo))
po_button2.grid(row=2, column=0, padx=5, pady=10)

# Code for PageTwo Content ####
pt_label = tk.Label(PageTwo, text="Page Two", font=LARGE_FONT)
pt_label.grid(row=0, column=0, padx=5, pady=10)
pt_button = tk.Button(PageTwo, text="Back To Start",
                      command=lambda: show_frame(StartPage))
pt_button.grid(row=1, column=0, padx=5, pady=10)
pt_button2 = tk.Button(PageTwo, text="Visit Page 1",
                       command=lambda: show_frame(PageOne))
pt_button2.grid(row=2, column=0, padx=5, pady=10)


show_frame(StartPage)
root.mainloop()
