import serial

a = []

with serial.Serial('/dev/cu.SLAB_USBtoUART', 230400, timeout = 1) as ser:
	while True:
		x = ser.read()
		a.append(x)
		print(x)	
		if x == 0xAA:
			x = ser.read()
			if x == 0x55:
				print(a)
				a = []
			else:
				a = []
				print("receive error")
