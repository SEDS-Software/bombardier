import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.title("Ground Station v1.0.0")
        master.iconbitmap("./logo.ico")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.abort_button = tk.Button(self)
        self.abort_button["text"] = "ABORT"
        self.abort_button["command"] = self.abort
        self.abort_button["bg"] = "red"
        self.abort_button.pack()

    def abort(self):
        print("Aborting Launch")

root = tk.Tk()
app = Application(master=root)
app.mainloop()