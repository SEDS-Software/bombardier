import tkinter as tk

def abort():
    print("Aborting Launch")

root = tk.Tk()
root.title("Ground Station v1.0.0")
root.iconbitmap("./logo.ico")

abort_button = tk.Button(root)
abort_button["text"] = "ABORT"
abort_button["command"] = abort
abort_button["bg"] = "red"
abort_button.pack()

root.mainloop()