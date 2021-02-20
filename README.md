# Bombardier Software

## GUI

![Current state of the gui](https://github.com/SEDS-Software/bombardier/blob/gui/status.png?raw=true)

### Computer Interface

- [x] Manual Abort
  - Will allow operator to manually abort launch
  - On-screen at all times in prominent location
- [x] Display the status of x valves
  - Use color coding (make sure operator is not color blind) to signify status for better usability
  - Possibly use indicators on the P&ID in place of labeling the valve statuses
- [ ] Countdown timer
  - Because countdown timers are really cool
  - Show elapsed time of rocket launch
  - Since time of launch will be short, only seconds and milliseconds will be needed
- [ ] Thermocouple temps
  - Display the main thermocouple temp updating as fast as possible (max update time 500ms | ideal update time <100ms)
  - Option to open a popup window with bar graph of all 7 thermocouples
  - Show temps in degrees C
  - Accuracy to the individual degree (decimal places are likely inaccurate and unnecessary)
- [ ] Thrust graph
  - Display the thrust data collected from the load cell in graph form
  - Graph should have scale labeled on axes
  - Possibly also graph modeled thrust curve from simulations to compare on-the-fly
- [ ] Pressure data
  - Display the pressure of all four pressure transducer
- [ ] Save live data to a file after launch
  - Everything sent to the laptop should be recorded

### Tech Stack

- Python
- Tkinter (because James knows how to use it)
- Serial coms (library undecided)
  - Must be able to access data via usb
  - Will be talking with arduino

### Physical Interface (LED Board for Pad Techs)

> We’ll get here when we get further in the project

## Data Collection

### Sensors we need data from:

- 6 Limit Switches (pneumatic valve states)
  - Arduino DIN
- 1 Potentiometer (motorized valve state)
  - Arduino AnalogIn
- 7 Thermocouples
  - DAQ board uses signal amplification/conditioning board MAX31855, which uses SPI. Arduino interfaces w these chips over SPI.
- 4 Pressure Transducers
  - On-device signal amplification/conditioning, producing either a voltage or current range output. If current (current plan[haha]), drop over a resistor to fit arduino AnalogIn.
- 1 Load Cell
  - mV output range, will need signal amplification/conditioning (see [Analog Front End document](https://drive.google.com/file/d/1mUZcVfHFdhDwAw1t8nDyquIU7wcV6O2l/view?usp=sharing))

## Communication

We have to decide on a communication hardware/softeare protocol. Currently considering:

- CAN
- Modbus TCP(over ethernet?)
- RS-232
- RS-485

We also have to decide whether we want communication to happen over a wired or wireless connection.
