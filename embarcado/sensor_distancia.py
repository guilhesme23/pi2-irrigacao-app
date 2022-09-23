#!usr/bin/python
#importar bibliotecas:
import RPi.GPIO as GPIO
import time

try:
	GPIO.setmode(GPIO.BOARD)
	#Variáveis para armazenar os pinos físicos
	PIN_TRIGGER = 7
	PIN_ECHO = 11
	buzzer = 23
	GPIO.setup(PIN_TRIGGER, GPIO.OUT) # trigger como saida
	GPIO.setup(PIN_ECHO, GPIO.IN) # echo como entrada
	GPIO.setup(buzzer, GPIO.OUT)

	GPIO.output(PIN_TRIGGER, GPIO.LOW) # Define o pino como LOW(não enviar nada para estabilizar)
	print ("Aguardando o sensor estabilizar")
	time.sleep(1) #pausa de 2s para o sensor estabilizar

	print ("Cálculo de distância")
	
	while True:
		GPIO.output(PIN_TRIGGER, GPIO.HIGH) #definir o pino em HIGH
		time.sleep(0.00001) # O pulso tera 10 ns
		GPIO.output(PIN_TRIGGER, GPIO.LOW) # suspende o pulso em seguida

		while GPIO.input(PIN_ECHO)==0: #Enquanto a entrada for LOW (0)
			pulse_start_time = time.time() #define a variavel como horario atual
		while GPIO.input(PIN_ECHO)==1: #Se a entrada for HIGH (1)
			pulse_end_time = time.time() #Define a variável como horário atual

		pulse_duration = pulse_end_time - pulse_start_time #A duracao do pulso como a diferenca entre o inicio de o fim
		distance = round(pulse_duration * 17000, 2) #distancia como sendo o tempo x velocidade/2 [cm]
		print ("Distancia: ",distance,"cm")
		time.sleep(0.1)
		if (distance < 50):
			print ("Obstáculo!")
			print("---------------------------------")
			GPIO.output(buzzer,1)
		else:
			GPIO.output(buzzer,0)

finally:
	GPIO.cleanup()

