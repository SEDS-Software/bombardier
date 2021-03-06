class State: # This class will hold all of the most up-to-date data on the rocket/test stand
	def __init__(self):
		self.valve = {
			"Main Valve": 1,
			"Vent Valve": 1,
			"Fuel Fill Valve": 0,
			"Pressurizing Valve": 0,
			"Drain Valve": 1
		}
		self.pt = [100, 200, 300, 400]
		self.tc = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

	# def update(self):

# For now all sensor data will be simulated in python so decoder,
# for the time being doesn't actually decode anything. It will,
# however, be used to interface with the arduino in the future.
# class decoder:
# 	def __init__(self):