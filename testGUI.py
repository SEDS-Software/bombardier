from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

import tkinter as tk
import pandas as pd
import numpy as np
import csv

#Define field names for csv files
fieldNames1 = ["time", "value"]
fieldNames2 = ["time 2", "value 2", "value 3"]
fieldNames3 = ["value 4"]

#Flags begin as false so the graphs don't start until button is pressed
lineplotFlag = False
lineplotFlag2 = False
barplotFlag = False
time1 = 0
time2 = 0
count = 1



def start():
    global count
    count = 0
    start_timer()

def start_timer():
    global count
    timer()

def stop():
    global count
    count = 1

def reset_timer():
    global count
    time.set("00:00")

def timer():
    global count
    if(count == 0):
        d = str(time.get())
        s,ms = map(int,d.split(":"))
        
        s = int(s)
        ms = int(ms)
        if(ms != 90):
            ms += 10
        else:
            ms = 0
            if(s < 59):
                s += 1
        if(s < 10):
            s = str(0) + str(s)
        else:
            s = str(s)
        if(ms < 10):
            ms = str(0) + str(ms)
        else:
            ms = str(ms)
        d = s + ":" + ms
        
        
        time.set(d)


            

def createPlot():
    global lineplotFlag, lineplotFlag2, barplotFlag, time1, time2

    #Creates a single line line graph
    if (lineplotFlag):
        start()
        #Generate random values to be graphed(Just for testing)
        value = np.random.rand()
        time1 = time1 + 0.1

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
        time2 = time2 + 0.1
        value2 = 10*np.random.rand() + 7
        value3 = 10*np.random.rand() + 3

        with open('randomLine2.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldNames2)

            info = {

                "time 2": time2,
                "value 2": value2,
                "value 3": value3

            }

            csv_writer.writerow(info)

        data2 = pd.read_csv('randomLine2.csv')

        a = data2['time 2']
        b = data2['value 2']
        c = data2['value 3']

        lines2.set_data(a, b)
        lines3.set_data(a, c)

        fig2.gca().relim()
        fig2.gca().autoscale_view()

        canvas2.draw()

    if(barplotFlag):
        value4 = np.random.rand() + 5
        #value5 = np.random.rand()

        with open('randomBar.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldNames3)

            info = {

                "value 4": value4

            }

            csv_writer.writerow(info)

        data3 = pd.read_csv('randomBar.csv')

        length = len(data3['value 4'])

        d = data3['value 4'][length - 1]

        bars.set_width(d)

        canvas3.draw()

    

    #Wait for 100 milliseconds then loop this function
    root.after(3, createPlot)

#Set flags to True to allow the graphs to begin graphing
def startPlot():
    global lineplotFlag, lineplotFlag2, barplotFlag
    

    if(~lineplotFlag):
        lineplotFlag = True

    if(~lineplotFlag2):
        lineplotFlag2 = True

    if(~barplotFlag):
        barplotFlag = True


#Set flags to false to stop plotting graphs
def stopPlot():
    global lineplotFlag, lineplotFlag2, barplotFlag
    if(lineplotFlag):
        lineplotFlag = False
    
    if(lineplotFlag2):
        lineplotFlag2 = False

    if(barplotFlag):
        barplotFlag = False

    stop()

def resetAll():
    stopPlot()
    reset_timer()

    with open('randomLine.csv', 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldNames1)
        csv_writer.writeheader()

    with open('randomLine2.csv', 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldNames2)
        csv_writer.writeheader()

    with open('randomBar.csv', 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldNames3)
        csv_writer.writeheader()

    lines.set_data([],[])
    fig.gca().relim()
    fig.gca().autoscale_view()

    lines2.set_data([],[])
    lines3.set_data([],[])
    fig2.gca().relim()
    fig2.gca().autoscale_view()

    bars.set_width(6)

    canvas.draw()
    canvas2.draw()
    canvas3.draw()


#GUI basic setup
root = tk.Tk()
root.title("Test Data Panel")
root.config(background = 'mint cream')
root.geometry("1920x1080")
time = tk.StringVar()
time.set("00:00")

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

fig2 = Figure()
ax2 = fig2.add_subplot(111)

ax2.set_title('Random Values')
ax2.set_xlabel('Time (Sec)')
ax2.set_ylabel('Random Value')
lines2, = ax2.plot([],[], label = 'Random Plus 7')
lines3, = ax2.plot([],[], label = 'Random Plus 3')
ax2.legend(loc='upper right')

canvas2 = FigureCanvasTkAgg(fig2, master=root) 
canvas2.get_tk_widget().place(x = 620, y = 10, width = 600, height = 400) 
canvas2.draw() 

fig3 = Figure()
ax3 = fig3.add_subplot(111)

ax3.set_title('Random Values')
ax3.set_ylabel('Random Value')
bars, = ax3.barh(range(1), 6, align = 'center')

canvas3 = FigureCanvasTkAgg(fig3, master=root) 
canvas3.get_tk_widget().place(x = 1230, y = 10, width = 600, height = 400) 
canvas3.draw()

root.update()
timerLabel = tk.Label(root, textvariable = time, font=("Courier", 25))
timerLabel.place(x=100, y=550)

#Add button to start the plotting of the graphs
root.update()
graphButton1 = tk.Button(root, text="Start Graphs", command=startPlot)
graphButton1.place(x=100, y=450)

#Add button to stop the plotting of the graphs
root.update()
graphButton2 = tk.Button(root, text="Stop Graphs", command=stopPlot)
graphButton2.place(x = 200, y = 450)

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
root.after(1, createPlot)
root.mainloop()
