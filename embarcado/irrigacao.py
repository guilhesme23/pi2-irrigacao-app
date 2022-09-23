import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

s_agua = 35
bomba = 15
buzzer = 23
cont = 0

GPIO.setup(s_agua, GPIO.IN)
GPIO.setup(bomba, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)

GPIO.output(bomba,0)
while True:
	cont+=1
	if cont == 1000:
		cont = 0
		if GPIO.input(s_agua) == 0:
			GPIO.output(bomba,1)
			print("Bomba ligada")
		else:
			GPIO.output(bomba,0)
			print("Bomba desligada")
