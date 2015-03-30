#!/usr/bin/env python

import sys
import serial
import time
import glob

preferred_list=['*']
# /dev/ttyASM*
# /dev/ttyUSB*
#glist = glob.glob('COM5')
#print glist[0]
connected = False
#ser = serial.Serial(port=glist[0], baudrate=9600)
ser = serial.Serial(port="COM5", baudrate=9600)
#ser = serial.Serial(port='/dev/tty.usbserial', baudrate=9600)
print ser.isOpen()
time.sleep(3)
ser.write('s')
#print ser.read()
ser.close();