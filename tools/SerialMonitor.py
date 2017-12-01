# simple serial console to debug the ternary clock firmware
# optimised for use on MacOS

from serial.tools import list_ports
import serial
import sys

comports =  list_ports.comports()

elementCounter = 0
print ' '
print ' '
print '-------------detected serial ports--------------'
for comport in comports:
    print '{0} : {1}'.format(elementCounter,comport[0].replace("cu","tty"))
    elementCounter += 1
print '------------------------------------------------'
#print serial.Serial.BAUDRATES                  # print a list with available baudrates

comport = elementCounter-1
comportName = comports[comport][0].replace("cu","tty")
usersChoice = raw_input('Please select the serial port to connect to ({0}) : '.format(comport))
if usersChoice.isdigit():
    usersChoice = int(usersChoice)
    if usersChoice in range(elementCounter):
        comportName = comports[usersChoice][0].replace("cu","tty")

linecounter = 0

print '------------------------------------------------'
print 'Connecting to {0} at 115200 baud'.format(comportName)
print 'Press ctrl-C to stop listening'
print '..........waiting for incoming messages.........'
print ' '

try:
    ser = serial.Serial(comportName, 115200)
    while True:
        try:
            message = ser.readline()
            print(message),
            linecounter += 1
        except KeyboardInterrupt:
            print ' '
            print 'Serial monitoring stopped.'
            break
    ser.close()
    print 'Port {0} closed.'.format(comportName)
except:
    print sys.exc_info()

print "-------------application ended------------------"
print '------------------------------------------------'
print ' '
