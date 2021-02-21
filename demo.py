import tkinter as tk
from PIL import Image
from PIL import ImageTk

w = 480
h = 640

green = '#66ff00'
red = '#ff2a1b'

led_size = 20

valves = [
	"Main Valve",
	"Vent Valve",
	"Fuel Fill Valve",
	"Pressurizing Valve",
	"Drain Valve"
]

# Where each indicator should appear on screen
valve_positions = [
	("Main Valve", 330, 365),
	("Vent Valve", 278, 185),
	("Fuel Fill Valve", 435, 220),
	("Pressurizing Valve", 330, 140),
	("Drain Valve", 260, 335)
]

pt_positions = [
	(0, 400, 115),
	(1, 305, 315),
	(2, 275, 430),
	(3, 275, 600)
]

tc_positions = [
	(0, 375, 315),
	(1, 401, 430),
	(2, 433, 443),
	(3, 465, 456),
	(4, 401, 469),
	(5, 433, 482),
	(6, 465, 495),
	(7, 401, 508),
	(8, 401, 545),
	(9, 401, 585)
]

# Contains the state of the sensors 
valve_states = {
	"Main Valve": 1,
	"Vent Valve": 1,
	"Fuel Fill Valve": 0,
	"Pressurizing Valve": 0,
	"Drain Valve": 1
}

pt_state = [100, 200, 300, 400]

tc_state = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# Update the indicator lights
def update():
	for key in rects:
		color = red if valve_states[key] == 0 else green
		canvas.itemconfig(rects[key], fill=color)

	for i in range(0, len(pts)):
		canvas.itemconfig(pts[i], text=str(pt_state[i]) + " psi")

	for i in range(0, len(tcs)):
		canvas.itemconfig(tcs[i], text=str(tc_state[i]) + " °C")

# Test function changing the state of a valve
def toggle_state():
	key = variable.get()
	valve_states[key] = 1 if valve_states[key] == 0 else 0
	update()

# Initialize window
root = tk.Tk()
root.title("Ground Station v1.0.0")
root.iconbitmap("logo.ico")
root.geometry(str(800) + "x" + str(640))

# Test valves
button = tk.Button(root, text="Open/Close Valve", bg="red", command=toggle_state)
variable = tk.StringVar(root)
variable.set(valves[0])
op_menu = tk.OptionMenu(root, variable, *valves)

# Create canvas
canvas = tk.Canvas(width=w, height=h)

# Add P&ID to canvas
img = Image.open("PID_valves.png")
img = img.resize((w,h), Image.ANTIALIAS)
photoImg =  ImageTk.PhotoImage(img)
canvas.create_image(0, 0, image=photoImg, anchor = tk.NW)

# Create indicators
rects = {}
for title, x, y in valve_positions:
	color = red if valve_states[title] == 0 else green
	rects[title] = canvas.create_rectangle(x, y, x+led_size, y+led_size, fill=color)

pts = []
for i, x, y in pt_positions:
	pts.append(canvas.create_text(x, y, text=str(pt_state[i]) + " psi"))

tcs = []
for i, x, y in tc_positions:
	tcs.append(canvas.create_text(x, y, text=str(tc_state[i]) + " °C"))

# Place everything in root widget
button.grid(row=0, column=0)
op_menu.grid(row=0, column=1)
canvas.grid(row=0, column=2)

root.mainloop()

