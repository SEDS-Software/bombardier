import tkinter as tk

valve_states = [
	("Main Valve", 1),
	("Vent Valve", 1),
	("Fuel Fill Valve", 0)
]

def abort():
    print("Aborting Launch")

root = tk.Tk()
root.title("Ground Station v1.0.0")
root.iconbitmap("./logo.ico")

abort_button = tk.Button(root, text="ABORT", bg="red", command=abort)
abort_button.pack()

valve_status_frame = tk.LabelFrame(root, text="Valve Statuses")
for name, state in valve_states:
	tk.Label(valve_status_frame, text=name).pack()
valve_status_frame.pack()

root.mainloop()