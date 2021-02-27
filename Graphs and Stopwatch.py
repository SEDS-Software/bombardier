#Figure to hold graphs to be loaded into GUI
from matplotlib.figure import Figure
#Allows matplotlib to interact with Tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#Imported incase we need to use datetime as axis
from matplotlib.dates import DateFormatter
#Used to obtain time for inputs and stop watch
from datetime import datetime

#Import tkinter for use in making GUI
import tkinter as tk
#Used to read data from csv
import pandas as pd
#Used to generate random values
import numpy as np
#Used to be able to use csv files
import csv


#Define field names for csv files
fieldNames1 = ["time", "value"]
fieldNames2 = ["time 2", "value 2", "value 3"]
fieldNames3 = ["value 4"]

#Flags begin as false so the graphs don't start until button is pressed
lineplotFlag = False
lineplotFlag2 = False
barplotFlag = False
stopFlag = False
RSFlag = True

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

#Set flags to True to allow the graphs to begin graphing
def startPlot():
    global lineplotFlag, lineplotFlag2, barplotFlag, startTime, RSFlag, stopTime, stopFlag

    #When pressing the start button make sure that stop and reset buttons are enabled
    graphButton2["state"] = "normal"
    graphButton3["state"] = "normal"
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

    graphButton1["state"] = "normal"


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


#GUI basic setup
root = tk.Tk()
root.title("Test Data Panel")
root.config(background = 'mint cream')
root.geometry("1920x1080")
time = tk.StringVar()
time.set("00:00.00")


#Create a figure object to be added to the GUI
fig = Figure()
ax = fig.add_subplot(111)

#Set aspects of the to-be-added graph 
ax.set_title('Random Values')
ax.set_xlabel('Time (Sec)')
ax.set_ylabel('Random Value')
lines, = ax.plot([],[])

#Add the graph to the GUI
canvas = FigureCanvasTkAgg(fig, master=root) 
canvas.get_tk_widget().place(x = 10, y = 10, width = 600, height = 400) 
canvas.draw() 

#Create new figure to contain our double line graph
fig2 = Figure()
ax2 = fig2.add_subplot(111)

ax2.set_title('Random Values')
ax2.set_xlabel('Time (Sec)')
ax2.set_ylabel('Random Value')
#Set up both lines as containing no values and set their names to designated values
lines2, = ax2.plot([],[], label = 'Random Plus 7')
lines3, = ax2.plot([],[], label = 'Random Plus 3')
ax2.legend(loc='upper right')

#Create a canvas object to contain the figure then add it to the GUI
canvas2 = FigureCanvasTkAgg(fig2, master=root) 
canvas2.get_tk_widget().place(x = 620, y = 10, width = 600, height = 400) 
canvas2.draw() 

#Create a figure to contain our one bar graph of default size 6
fig3 = Figure()
ax3 = fig3.add_subplot(111)

ax3.set_title('Random Values')
ax3.set_ylabel('Random Value')
bars, = ax3.barh(range(1), 6, align = 'center')

#Create and add bar graph figure to our GUI
canvas3 = FigureCanvasTkAgg(fig3, master=root) 
canvas3.get_tk_widget().place(x = 1230, y = 10, width = 600, height = 400) 
canvas3.draw()

#Add our stopwatch to GUI as a label 
root.update()
#Use textvariable to be able to update text with new times
timerLabel = tk.Label(root, textvariable = time, font=("Courier", 40))
timerLabel.place(x=730, y=450)

#Add button to start the plotting of the graphs
root.update()
graphButton1 = tk.Button(root, text="Start Graphs", command=startPlot)
graphButton1.place(x=100, y=450)

#Add button to stop the plotting of the graphs
root.update()
graphButton2 = tk.Button(root, text="Stop Graphs", command=stopPlot)
graphButton2.place(x = 200, y = 450)

#Add button to allow us to stop and reset all features of GUI
root.update()
graphButton3 = tk.Button(root, text = "Stop and Reset Graphs", command=resetAll)
graphButton3.place(x = 300, y = 450)

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
root.after(1, createGUI)
root.mainloop()
