#Figure to hold graphs to be loaded into GUI
from matplotlib.figure import Figure
#Allows matplotlib to interact with Tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#Imported incase we need to use datetime as axis
from matplotlib.dates import DateFormatter
#Used to obtain time for inputs and stop watch
from datetime import datetime
#Used to handle images in Tkinter
from PIL import ImageTk, Image

#Import tkinter for use in making GUI
import tkinter as tk
#Used to read data from csv
import pandas as pd
#Used to generate random values
import numpy as np
#Used to be able to use csv files
import csv
#Used to restart the program after process is aborted
import sys
import os

from pid_frame import PIDFrame
#Handles the state for everything displayed on the gui
from serial_decoder import State


#Define field names for csv files
fieldNames1 = ["time", "value"]
fieldNames2 = ["time 2", "value 2", "value 3"]
fieldNames3 = ["value 4"]

#Create state object
state = State()

#Some colors for the valve labels
red = "red"
green = "lawn green"

#Flags begin as false so the graphs don't start until button is pressed
lineplotFlag = False
lineplotFlag2 = False
barplotFlag = False
stopFlag = False
RSFlag = True
startFlag = False
pressureFlag, ventFlag, fuelFlag, drainFlag, mainFlag = False, False, False, False, False

#Define times for input x values
time1 = 0
time2 = 0

#main function to run our GUI
def createGUI():
    global lineplotFlag, lineplotFlag2, barplotFlag, time1, time2, startTime, time

    #Creates a single line line graph
    if (lineplotFlag):

        #Generate random values to be graphed
        value = np.random.rand()
        time1 = time1 + 0.1

        #Save the time that this operation is running
        time1Obj = datetime.now()
        #Find how much time has elapsed since the program started
        timeDif = time1Obj - startTime
        #Update stop watch with current time elapsed
        time.set(str(timeDif)[2:10])

        #Open the corresponding csv file and add the generated values (Just for testing)
        with open('randomLine.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldNames1)

            info = {

                "time": time1,
                "value": value

            }

            csv_writer.writerow(info)

        #Read the csv file and save the data as 2D array
        data = pd.read_csv('randomLine.csv')
        x = data['time']
        y = data['value']

        #Update the values that are used in the line graph with the newly generated values
        lines.set_data(x, y)

        #Rescale the axis of the line graph
        fig.gca().relim()
        fig.gca().autoscale_view()

        #Redraw the figure to update the graph on the GUI
        canvas.draw()

    if(lineplotFlag2):
        #Generate values to be graphed
        time2 = time2 + 0.1
        value2 = 10*np.random.rand() + 7
        value3 = 10*np.random.rand() + 3

        #Find time that this process has taken place
        time2Obj = datetime.now()

        #Update the time elapsed
        timeDif = time2Obj - startTime
        #Update time on stopwatch
        time.set(str(timeDif)[2:10])

        #Add values to second csv
        with open('randomLine2.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldNames2)

            info = {

                "time 2": time2,
                "value 2": value2,
                "value 3": value3

            }

            csv_writer.writerow(info)

        #Read and save values to input arrays
        data2 = pd.read_csv('randomLine2.csv')

        a = data2['time 2']
        b = data2['value 2']
        c = data2['value 3']

        #Update arrays that are used to graph the lines
        lines2.set_data(a, b)
        lines3.set_data(a, c)

        #Rescale axis
        fig2.gca().relim()
        fig2.gca().autoscale_view()

        #Redraw figure on GUI
        canvas2.draw()

    if(barplotFlag):
        #Generate random value for bar graph
        value4 = np.random.rand() * 6

        #Find and update time elapsed
        time3 = datetime.now()
        timeDif = time3 - startTime

        #Update stopwatch
        time.set(str(timeDif)[2:10])

        #Add generated value to csv
        with open('randomBar.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldNames3)

            info = {

                "value 4": value4

            }

            csv_writer.writerow(info)

        #read data from csv
        data3 = pd.read_csv('randomBar.csv')

        #Find the number of elements in the array 
        length = len(data3['value 4'])

        #Find the last element in the data array to obtain the new height of the bar graph
        d = data3['value 4'][length - 1]

        #Update the bar graph
        bars.set_width(d)

        #Redraw the figure on the GUI
        canvas3.draw()

    #Wait for 100 milliseconds then loop this function
    root.after(100, createGUI)

#Function to create popup window containing all graphs
def popupWindow():
    global lines, lines2, lines3, bars, fig, fig2, fig3, canvas, canvas2, canvas3, popup
    popup = tk.Toplevel()
    popup.title("Graphs of Data")
    popup.minsize(1920, 1080)
    popup.config(background= 'light slate gray')

    #Create a figure object to be added to the GUI
    fig = Figure()
    ax = fig.add_subplot(111)

    #Set aspects of the to-be-added graph 
    ax.set_title('Single Line Graph')
    ax.set_xlabel('Time (Sec)')
    ax.set_ylabel('Random Value')
    lines, = ax.plot([],[])

    #Add the graph to the GUI
    canvas = FigureCanvasTkAgg(fig, master=popup) 
    canvas.get_tk_widget().place(x = 10, y = 10, width = 600, height = 400) 
    canvas.draw() 

    #Create new figure to contain our double line graph
    fig2 = Figure()
    ax2 = fig2.add_subplot(111)

    ax2.set_title('Double Line Graph')
    ax2.set_xlabel('Time (Sec)')
    ax2.set_ylabel('Random Value')
    #Set up both lines as containing no values and set their names to designated values
    lines2, = ax2.plot([],[], label = 'Random Plus 7')
    lines3, = ax2.plot([],[], label = 'Random Plus 3')
    ax2.legend(loc='upper right')

    #Create a canvas object to contain the figure then add it to the GUI
    canvas2 = FigureCanvasTkAgg(fig2, master=popup) 
    canvas2.get_tk_widget().place(x = 620, y = 10, width = 600, height = 400) 
    canvas2.draw() 

    #Create a figure to contain our one bar graph of default size 6
    fig3 = Figure()
    ax3 = fig3.add_subplot(111)

    ax3.set_title('Bar Graph')
    ax3.set_xlabel('Random Value')
    bars, = ax3.barh(range(1), 6, align = 'center')

    #Create and add bar graph figure to our GUI
    canvas3 = FigureCanvasTkAgg(fig3, master=popup) 
    canvas3.get_tk_widget().place(x = 1230, y = 10, width = 600, height = 400) 
    canvas3.draw()

    #Ensure that user cannot close out of popup window without pressing designated button
    popup.protocol("WM_DELETE_WINDOW", disableEvent)

    createGUI()
    popup.mainloop()

#Function to manually close popup window and reset start button
def closePopup():
    global popup, startFlag
    startFlag = False
    popup.destroy()
    graphButton1["state"] = "normal"

#This changes the X button of the popup window to do nothing instead of exiting
def disableEvent():
    pass

#Set flags to True to allow the graphs to begin graphing
def startPlot():
    global lineplotFlag, lineplotFlag2, barplotFlag, startTime, RSFlag, stopTime, stopFlag, startFlag

    #When pressing the start button make sure all graph realated buttons are enabled
    graphButton2["state"] = "normal"
    graphButton3["state"] = "normal"
    graphButton4["state"] = "normal"
    graphButton1["state"] = "disabled"


    #Find the time the program starts and only run at the beginning or after the graphs are reset
    if(RSFlag):
        startTime = datetime.now()
        RSFlag = False

    #If the stop button is pressed, save the current time on the stopwatch so that if we press start again, the time does not change
    if(stopFlag):
        startTime2 = datetime.now()
        timeDelta = startTime2 - stopTime
        startTime = startTime + timeDelta
        stopFlag = False

    #Set flags for all instances in order for all graphs to begin graphing
    if(not lineplotFlag):
        lineplotFlag = True

    if(not lineplotFlag2):
        lineplotFlag2 = True

    if(not barplotFlag):
        barplotFlag = True

    #When you press start for the first time, create the popup window containing graphs
    if(not startFlag):
        startFlag = True
        popupWindow()


#Set flags to false to stop plotting graphs
def stopPlot():
    global lineplotFlag, lineplotFlag2, barplotFlag, stopTime, stopFlag, RSFlag

    #Set flags for all instances to stop all graphs from graphing
    if(lineplotFlag):
        lineplotFlag = False
    
    if(lineplotFlag2):
        lineplotFlag2 = False

    if(barplotFlag):
        barplotFlag = False

    #If the stop button was pressed, then save the time that it was pressed and disable the stop and reset button
    if(not RSFlag):
        stopTime = datetime.now()
        stopFlag = True
        graphButton3["state"] = "disabled"
        graphButton2["state"] = "disabled"

    graphButton1["state"] = "normal"

#Function that will stop all processes and prevent the user from further imputs.
def abort():
    global photoLabel2
    #Only stop graphs if graphs were started
    if(startFlag):
        stopPlot()

    #Change the status image to designated status image
    image3 = Image.open("Frown.png")
    image3 = image3.resize((100, 100), Image.ANTIALIAS)
    photoImg3 = ImageTk.PhotoImage(image3)

    photoLabel2.config(image = photoImg3)
    photoLabel2.config(text = "Status: ABORTED")
    photoLabel2.image = photoImg3

    #Disable all buttons so that user cannot input anything else
    graphButton1["state"] = "disabled"
    graphButton2["state"] = "disabled"
    graphButton3["state"] = "disabled"
    graphButton4["state"] = "disabled"
    valveButton6["state"] = "disabled"
    valveButton7["state"] = "disabled"

    #Disable all valve indicators regardless of status
    pid_frame.updateValves(0)

    #Display text showing that the program was aborted and what to do.
    GUILabel = tk.Label(root, text = "Program aborted. Restart to reset.")
    GUILabel.config(bg= "seashell2")
    GUILabel.config(relief = "solid")
    GUILabel.place(x = 50, y = 600)

    #Change abort button to be a restart button that restarts program
    graphButton5.config(text = "RESTART")
    graphButton5.config(width = 7)
    graphButton5.config(command = restartButton)
    

#Code to reset all graphs, CSVs, and the stopwatch
def resetAll():
    global time1, time2, RSFlag
    if(not stopFlag):
        #After reseting allow the stopwatch to recalibrate its starting time
        RSFlag = True

        graphButton2["state"] = "disabled"

        #Stop plotting the data
        stopPlot()

        #Clear the CSVs by recreating the CSVs with no data points
        with open('randomLine.csv', 'w', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldNames1)
            csv_writer.writeheader()

        with open('randomLine2.csv', 'w', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldNames2)
            csv_writer.writeheader()

        with open('randomBar.csv', 'w', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldNames3)
            csv_writer.writeheader()

        #Reset starting variables
        time1 = 0
        time2 = 0

        #Reset the text of our stopwatch to the starting value
        time.set('00:00.00')

        #Reset the single line graph to being empty
        lines.set_data([],[])
        fig.gca().relim()
        fig.gca().autoscale_view()

        #Reset the double line graph to being empty
        lines2.set_data([],[])
        lines3.set_data([],[])
        fig2.gca().relim()
        fig2.gca().autoscale_view()

        #Set bar graph to default width
        bars.set_width(6)

        #Redraw all graphs back onto the GUI
        canvas.draw()
        canvas2.draw()
        canvas3.draw()

#Function to check the current status of the selected valve and set button values appropriately
def checkValveState(filler):
    global variable
    #Get the current value of the dropdown menu
    currValve = variable.get()
    if(currValve == "All Valves"):
        valveButton6["state"] = "normal"
        valveButton7["state"] = "normal"
    else:
        valveButton6["state"] = "disabled" if state.valve[currValve] == 1 else "normal"
        valveButton7["state"] = "disabled" if state.valve[currValve] == 0 else "normal"

#Depending on the valve selected, "open" the valve
def controlOpen():
    currValve = variable.get()
    if(currValve == "All Valves"):
        pid_frame.updateValves(1)
    else:
        pid_frame.updateValve(currValve, 1)

    valveButton6["state"] = "disabled"
    valveButton7["state"] = "normal"

#Depending on the valve selected, "close" the valve
def controlClose():
    currValve = variable.get()
    if(currValve == "All Valves"):
        pid_frame.updateValves(0)
    else:
        pid_frame.updateValve(currValve, 0)

    valveButton6["state"] = "normal"
    valveButton7["state"] = "disabled"

def restartButton():
    #Restarts the current program.
    python = sys.executable
    os.execl(python, python, * sys.argv)
    

#GUI basic setup
root = tk.Tk()
root.title("User Control Panel")
root.iconbitmap("logo.ico")
root.config(background = 'light slate gray')
root.geometry("950x670")
root.resizable(0, 0)
time = tk.StringVar()
time.set("00:00.00")

#Add our stopwatch to GUI as a label 
root.update()
#Use textvariable to be able to update text with new times
timerLabel = tk.Label(root, textvariable = time, font=("Courier", 40), relief = "solid")
timerLabel.place(x=100, y=75)

#Add button to start the plotting of the graphs
root.update()
graphButton1 = tk.Button(root, text="Display/Start Graphs", command=startPlot)
graphButton1.place(x=75, y=175)

#Add button to stop the plotting of the graphs
root.update()
graphButton2 = tk.Button(root, text="Stop Graphs", command=stopPlot)
graphButton2.place(x = 197, y = 175)
graphButton2["state"] = "disabled"

#Add button to allow us to stop and reset all features of GUI
root.update()
graphButton3 = tk.Button(root, text = "Stop and Reset Graphs", command=resetAll)
graphButton3.place(x = 275, y = 175)
graphButton3["state"] = "disabled"

#Add button to close the popup window containing graphs
root.update()
graphButton4 = tk.Button(root, text = "Close Graphs", command=closePopup)
graphButton4.place(x = 197, y = 225)
graphButton4["state"] = "disabled"

#Add Abort button to stop all processes WIP
root.update()
graphButton5 = tk.Button(root, text = "ABORT", font = ("Courier", 25), background = 'red', command=abort)
graphButton5.config(height = 1, width = 6)
graphButton5.place(x = 65, y = 525)

# Add PID Frame for displaying sensor data
pid_frame = PIDFrame(root, state)
pid_frame.place(x = 450, y = 10)

#Add image to show status of program at all times
image2 = Image.open("Smile.png")
image2 = image2.resize((100, 100), Image.ANTIALIAS)
photoImg2 = ImageTk.PhotoImage(image2)
photoLabel2 = tk.Label(root, text = "Status: All Good", image = photoImg2, compound = "bottom")
photoLabel2.config(bg= "light slate gray")
photoLabel2.config(relief = "ridge")
photoLabel2.place(x = 250, y = 510)

valves = [
    "Pressurizing Valve",
    "Vent Valve",
    "Fuel Fill Valve",
    "Drain Valve",
    "Main Valve",
    "All Valves"
]

#Sets the default value of the dropdown menu to be the first item on the list
variable = tk.StringVar(root)
variable.set(valves[0])

#Create and place dropdown menu onto the GUI
valveDropdown = tk.OptionMenu(root, variable, *valves, command = checkValveState)
valveDropdown.place(x = 230, y = 300)

#Create and place open valve button onto the GUI
root.update()
valveButton6 = tk.Button(root, text = "Open Valve", font = ("Courier", 12), command=controlOpen)
valveButton6.config(width = 12, height = 2)
valveButton6.place(x = 75, y = 300)

#Create and place the close valve button onto the GUI and set it as default disabled
root.update()
valveButton7 = tk.Button(root, text = "Close Valve", font = ("Courier", 12), command=controlClose)
valveButton7.config(width = 12, height = 2)
valveButton7.place(x = 75, y = 350)
valveButton7["state"] = "disabled"


#Open all the csv files needed and set the field names to the desired fields
with open('randomLine.csv', 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldNames1)
    csv_writer.writeheader()

with open('randomLine2.csv', 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldNames2)
    csv_writer.writeheader()

with open('randomBar.csv', 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldNames3)
    csv_writer.writeheader()


#Immediately run the main section of code after setup is complete
root.mainloop()
