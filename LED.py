#/*
#Python and Tkinter Programming
#John E. Grayson

#ISBN: 1884777813
#Publisher: Manning
#*/
from tkinter import *

SQUARE      = 1
ROUND       = 2

STATUS_OFF   = 1
STATUS_ON    = 2
STATUS_SET   = 5

class DummyClass:
    pass

Color  = DummyClass()

Color.PANEL     = '#545454'
Color.OFF       = '#656565'
Color.ON        = '#00FF33'

class LED:
    def __init__(self, master=None, width=25, height=25,
                 status=STATUS_ON, 
                 bg=None, 
                 shape=SQUARE, outline="",
                 blink=0, blinkrate=1,
                 takefocus=0):
        # preserve attributes
        self.master       = master
        self.shape        = shape
        self.onColor      = Color.ON
        self.offColor     = Color.OFF
        self.specialColor = '#00ffdd'
        self.status       = status
        self.blink        = blink
        self.blinkrate    = int(blinkrate)
        self.on           = 0
        self.onState      = None

        if not bg:
            bg = Color.PANEL

        ## Base frame to contain light
        self.frame=Frame(master, relief=FLAT, bg=bg, 
                         takefocus=takefocus)

        basesize = width
        d = center = int(basesize/2)

        if self.shape == SQUARE:
            self.canvas=Canvas(self.frame, height=height, width=width, 
                               bg=bg, bd=0, highlightthickness=0)

            self.light=self.canvas.create_rectangle(0, 0, width, height,
                                                    fill=Color.ON)
        elif self.shape == ROUND:
            r = int((basesize-2)/2)
            self.canvas=Canvas(self.frame, width=width, height=width, 
                               highlightthickness=0, bg=bg, bd=0)
            if bd > 0:
                self.border=self.canvas.create_oval(center-r, center-r, 
                                                    center+r, center+r)
                r = r - bd
            self.light=self.canvas.create_oval(center-r-1, center-r-1, 
                               center+r, center+r, fill=Color.ON,
                               outline=outline)
        
        self.canvas.pack(side=TOP, fill=X, expand=NO)
        self.update()

    def turnon(self):
        self.status = STATUS_ON
        if not self.blink: self.update()

    def turnoff(self):
        self.status = STATUS_OFF
        if not self.blink: self.update()

    def set(self, color):
        self.status       = STATUS_SET
        self.specialColor = color
        self.update()

    def blinkon(self):
        if not self.blink:
            self.blink   = 1
            self.onState = self.status
            self.update()

    def blinkoff(self):
        if self.blink:
            self.blink   = 0
            self.status  = self.onState
            self.onState = None
            self.on      = 0
            self.update()

    def blinkstate(self, blinkstate):
        if blinkstate:
            self.blinkon()
        else:
            self.blinkoff()

    def update(self):
        # First do the blink, if set to blink
        if self.blink:
            if self.on:
                if not self.onState:
                    self.onState = self.status
                self.status  = STATUS_OFF
                self.on      = 0                            
            else:
                if self.onState:
                    self.status = self.onState     # Current ON color
                self.on = 1

        if self.status == STATUS_ON:
            self.canvas.itemconfig(self.light, fill=self.onColor)
        elif self.status == STATUS_OFF:
            self.canvas.itemconfig(self.light, fill=self.offColor)
        elif self.status == STATUS_SET:
            self.canvas.itemconfig(self.light, fill=self.specialColor)

        self.canvas.update_idletasks()

        if self.blink:
            self.frame.after(self.blinkrate * 1000, self.update)