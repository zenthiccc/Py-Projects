import tkinter as tk
from tkinter import filedialog, Text
import os

top = tk.Tk()
top.title("Program Executer")
apps = []


def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    for app in apps:
        global label
        label = tk.Label(frame, text=app, bg="gray", anchor="w")
        label.pack()

    runButton.config(state="normal")
    deleteButton.config(state="normal")

def runApp():
    for app in apps:
        os.startfile(app)

def deleteApp():
    for widget in frame.winfo_children():
        widget.destroy()
    del apps[:]
    deleteButton.config(state="disabled")
    runButton.config(state="disabled")


canvas = tk.Canvas(top, height=400, width=800)
canvas.pack()

frame = tk.Frame(top, bg="gray")
frame.place(relwidth=1, relheight=1, relx=0.15, )



openButton= tk.Button(top, text="Open App", font="Calibri", fg="black", bg="#33FF49", command=addApp)
openButton.place(relwidth=0.15, relheight=0.1)

runButton = tk.Button(top, text="Run App", font="Calibri", fg="black", bg="gray", command=runApp, state="disabled")
runButton.place(relwidth=0.15, relheight=0.1, rely=0.1)

deleteButton = tk.Button(top, text="Delete App", font="Calibri", fg="black", bg="red", command=deleteApp, state="disabled")
deleteButton.place(relwidth=0.15, relheight=0.1, rely=0.2)

top.mainloop()


