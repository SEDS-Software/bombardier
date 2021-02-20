import tkinter as tk
from LED import *

valve_states = [
	("Main Valve", 1),
	("Vent Valve", 1),
	("Fuel Fill Valve", 0),
	("Pressurizing Valve", 0),
	("Drain Valve", 1)
]

def abort():
    print("Aborting Launch")

# Initialize window
root = tk.Tk()
root.title("Ground Station v1.0.0")
root.iconbitmap("./logo.ico")
root.geometry("1280x720")

# Create abort button
abort_button = tk.Button(root, text="ABORT", bg="red", command=abort)
abort_button.pack()

# Create valve status frame
valve_status_frame = tk.LabelFrame(root, text="Valve Statuses")
for i in range(0, len(valve_states)):
	tk.Label(valve_status_frame, text=valve_states[i][0]).grid(row=i, column=0)
	status = STATUS_OFF if valve_states[i][1] == 0 else STATUS_ON
	LED(valve_status_frame, shape=SQUARE, status=status,
		width=20, height=20).frame.grid(row=i, column=1, padx=10, pady=5)
valve_status_frame.pack()


root.mainloop()