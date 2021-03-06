class State: # This class will hold all of the most up-to-date data on the rocket/test stand
	def __init__(self):
		self.dec = Decoder()
		# Initializes everything to default values
		self.valve = {
			"Main Valve": 1,
			"Vent Valve": 1,
			"Fuel Fill Valve": 0,
			"Pressurizing Valve": 0,
			"Drain Valve": 1
		}
		self.pt = [100, 200, 300, 400]
		self.tc = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

	# This function will eventually send a command to the test stand in addition to updating state
	def set_valve(self, valve, new_state):
		self.valve[valve] = new_state

	def update(self):
		self.pt = self.dec.get_pt_data()

# For now all sensor data will be simulated in python so decoder,
# for the time being doesn't actually decode anything. It will,
# however, be used to interface with the arduino in the future.
class Decoder:
	def __init__(self):
		pass

	# Simulates pressure transducer senseor data
	def get_pt_data(self):
		return [2, 3, 4, 5]
