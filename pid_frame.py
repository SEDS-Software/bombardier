import tkinter as tk
from PIL import Image
from PIL import ImageTk

from serial_decoder import State

w = 480
h = 640

red = "red"
green = "lawn green"

led_size = 20

valves = [
    "Pressurizing Valve",
    "Vent Valve",
    "Fuel Fill Valve",
    "Drain Valve",
    "Main Valve"
]

# These vars are only used once to place the elements on the canvas
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

class PIDFrame(tk.Frame):

	def __init__(self, parent, state):
		tk.Frame.__init__(self, parent)
		# Create canvas and pid image
		self.canvas = tk.Canvas(self, width=w, height=h)
		self.image = Image.open("PID_valves.png")
		self.image = self.image.resize((w, h), Image.ANTIALIAS)
		self.photoImg = ImageTk.PhotoImage(self.image)
		self.canvas.create_image(0, 0, image=self.photoImg, anchor = tk.NW)
		self.canvas.config(bg = "seashell2")
		# Create valve indicators
		self.valveLabels = {}
		for valve, x, y in valve_positions:
			color = red if state.valve[valve] == 0 else green
			self.valveLabels[valve] = self.canvas.create_rectangle(x, y, x+led_size, y+led_size, fill=color)
		# Create pt indicators
		self.pts = []
		for i, x, y in pt_positions:
			self.pts.append(self.canvas.create_text(x, y, text=str(state.pt[i]) + " psi"))
		# Create tc indicators
		self.tcs = []
		for i, x, y in tc_positions:
			self.tcs.append(self.canvas.create_text(x, y, text=str(state.tc[i]) + " °C"))
		# Place canvas in frame
		self.canvas.pack()

	# Use update instead
	def update_valves(self, new_state):
	    for valve in valves:
	        self.update_valve(valve, new_state)

	# Use update instead
	def update_valve(self, valve, new_state):
	    color = red if new_state == 0 else green
	    self.canvas.itemconfig(self.valveLabels[valve], fill=color)

	# Updates all gui elements given the new state
	def update(self, state):
		for valve in state.valve:
			update_valve(valve, state.valve[valve])
