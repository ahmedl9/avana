
#print("Hello World")

import serial

def myRead(mySerial):
	serialIn = int(mySerial.readline().decode('unicode_escape'))
	if serialIn < 0:
		return "Button"
	elif serialIn > 500 and serialIn < 540:
		return "Still"
	elif serialIn >= 540:
		return "Right"
	else:
		return "Left"


#ser = serial.Serial('/dev/cu.usbmodem1411', 115200)

#while True:
	#print(myRead(ser))

