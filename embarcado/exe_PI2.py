#========================== Motor PWM =============================
import RPi.GPIO as GPIO
import smbus		#import SMBus module of I2C
import time
from math import atan2
from math import pow
from math import sqrt


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# escolha dos pinos
enableA_pin = 29    
in_1_pin = 31
in_2_pin = 33

enableB_pin = 22   
in_3_pin = 12
in_4_pin = 16

duty_baseA = 40
duty_baseB = 55

#Definicao dos pinos como saida
GPIO.setup(enableA_pin, GPIO.OUT)
GPIO.setup(in_1_pin, GPIO.OUT)
GPIO.setup(in_2_pin, GPIO.OUT)

GPIO.setup(enableB_pin, GPIO.OUT)
GPIO.setup(in_3_pin, GPIO.OUT)
GPIO.setup(in_4_pin, GPIO.OUT)

motorA_pwm = GPIO.PWM(enableA_pin, 300)
motorB_pwm = GPIO.PWM(enableB_pin, 300)

motorA_pwm.start(0)
motorB_pwm.start(0)

#Peso do giroscopio no filtro complementar
peso_giro = 0.98 
const_gravid = 9.81

#Variaveis de tempo
tempo_i = 0
tempo_f = 0
dT = 0
cont = 0

def anda_irriga():
	forward()
	time.sleep(1)
	spin()
	time.sleep(1)
	Irrigar()
	time.sleep(1)
	forward()
	time.sleep(1)
	spin()

def forward():          
	GPIO.output(in_1_pin, False) 
	GPIO.output(in_2_pin, True) 
	GPIO.output(in_3_pin, False) 
	GPIO.output(in_4_pin, True)     
	motorA_pwm.ChangeDutyCycle(75) #Esquerdo (38)
	motorB_pwm.ChangeDutyCycle(85) #Direito  (58)
	#time.sleep(0.5)
	#motorA_pwm.ChangeDutyCycle(70) #Esquerdo (38)
	#motorB_pwm.ChangeDutyCycle(80) #Direito  (58)
	mpu6050_forward()
	#time.sleep(3)
	motorA_pwm.ChangeDutyCycle(0)
	motorB_pwm.ChangeDutyCycle(0)    
    
def spin():          
	GPIO.output(in_1_pin, False) 
	GPIO.output(in_2_pin, True) 
	GPIO.output(in_3_pin, True) 
	GPIO.output(in_4_pin, False)  
	motorA_pwm.ChangeDutyCycle(85) # 40
	motorB_pwm.ChangeDutyCycle(40) # 40
	mpu6050_spin()
	motorA_pwm.ChangeDutyCycle(0)
	motorB_pwm.ChangeDutyCycle(0)
	
def reverse():          
	GPIO.output(in_1_pin, True) 
	GPIO.output(in_2_pin, False) 
	GPIO.output(in_3_pin, True) 
	GPIO.output(in_4_pin, False)     
	motorA_pwm.ChangeDutyCycle(40) #~5V
	motorB_pwm.ChangeDutyCycle(40) #~5V
	time.sleep(3)
	motorA_pwm.ChangeDutyCycle(0)
	motorB_pwm.ChangeDutyCycle(0) 
	
#======================== Sendor ultrassonico =========================
PIN_TRIGGER = 7 #Variáveis para armazenar os pinos físicos
PIN_ECHO = 11
buzzer = 23
GPIO.setup(PIN_TRIGGER, GPIO.OUT) # trigger como saida
GPIO.setup(PIN_ECHO, GPIO.IN) # echo como entrada
GPIO.setup(buzzer, GPIO.OUT)

def sonar():
	#GPIO.output(bomba,0)
	GPIO.output(PIN_TRIGGER, GPIO.LOW) # Define o pino como LOW(não enviar nada para estabilizar)
	#print ("Aguardando o sensor estabilizar")
	#time.sleep(2) #pausa de 2s para o sensor estabilizar
	print ("Cálculo de distância")

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
	
	if (distance < 50):
		print ("Obstáculo!")
		print("---------------------------------")
		motorA_pwm.ChangeDutyCycle(0)
		motorB_pwm.ChangeDutyCycle(0)
		GPIO.output(buzzer,1)
	else:
		GPIO.output(buzzer,0)
		motorA_pwm.ChangeDutyCycle(65)
		motorB_pwm.ChangeDutyCycle(85)


	
#============================== Irrigação =============================
s_agua = 35
bomba = 15

GPIO.setup(s_agua, GPIO.IN)
GPIO.setup(bomba, GPIO.OUT)

def Irrigar():
	GPIO.output(bomba,0)
	while True:
		if GPIO.input(s_agua) == 0:
			GPIO.output(bomba,1)
			print("Bomba ligada")
		else:
			GPIO.output(bomba,0)
			print("Bomba desligada")
			print("---------------------------------")
			break
		time.sleep(1)
    
#============================== MPU6050 ===============================

#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
TEMP_OUT0    = 0x41
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47

def MPU_Init():
	#write to sample rate register
	bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)

	#Write to power management register
	bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)

	#Write to Configuration register
	bus.write_byte_data(Device_Address, CONFIG, 0)

	#Write to Gyro configuration register
	bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)

	#Write to interrupt enable register
	bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
	#Accelero and Gyro value are 16-bit
	high = bus.read_byte_data(Device_Address, addr)
	low = bus.read_byte_data(Device_Address, addr+1)

	#concatenate higher and lower value
	value = ((high << 8) | low)

	#to get signed value from mpu6050
	if(value > 32768):
		value = value - 65536
	return value

bus = smbus.SMBus(1)
Device_Address = 0x68   # MPU6050 device address

MPU_Init()

#===================================== MPU6050_forward =========================================
def mpu6050_forward():
	print (" Reading Data of Gyroscope and Accelerometer")
	cont = 0
	ang_x_prev = 0
	ang_y_prev = 0
	ang_z_prev = 0
	ang_x = 0
	ang_y = 0
	ang_z = 0
	vel = 0
	vel_prev = 0
	dist = 0
	dist_prev = 0
	tempo_i = 0
	tempo_f = 0
	dT = 0
	x = 0
	
	while True:
		#sonar()
		tempo_i = time.time() #contar tempo do loop
		
		#Read Accelerometer raw value
		acc_x = read_raw_data(ACCEL_XOUT_H)
		acc_y = read_raw_data(ACCEL_YOUT_H)
		acc_z = read_raw_data(ACCEL_ZOUT_H)
		
		Ax = acc_x/16384.0 #32768/2
		Ay = acc_y/16384.0 #32768/2
		Az = acc_z/16384.0 #32768/2
		
		#Read Gyroscope raw value
		gyro_x = read_raw_data(GYRO_XOUT_H)
		gyro_y = read_raw_data(GYRO_YOUT_H)
		gyro_z = read_raw_data(GYRO_ZOUT_H)	
		
		Gx = gyro_x/131.0 #32768/250
		Gy = gyro_y/131.0 #32768/250
		Gz = gyro_z/131.0 #32768/250
		
		#Calcula a inclinacao a partir da gravidade
		AccXangle = (atan2(acc_x, sqrt(pow(acc_y,2) + pow(acc_z,2)))*180)/3.14
		AccYangle = (atan2(acc_y, sqrt(pow(acc_x,2) + pow(acc_z,2)))*180)/3.14
		AccZangle = (atan2(acc_z, sqrt(pow(acc_x,2) + pow(acc_y,2)))*180)/3.14
		
		
		#Fusão dos dados: giro + accel
		#Método: filtro complementar:
		#Atribui peso de 0.98 ao valor do giro e 0.02 ao acelerometro
		#CFangleX=peso_giro*(CFangleX+Gx*(dT/1000))+(1-peso_giro) * AccXangle
		#CFangleY=peso_giro*(CFangleY+Gy*(dT/1000))+(1-peso_giro) * AccYangle
		#CFangleZ=peso_giro*(CFangleZ+Gz*(dT/1000))+(1-peso_giro) * AccZangle
		
#============================== MPU6050_Angulo ==================================
		if abs(Gz)>0.2:		
			#Calculo do angulo de rotacao
			ang_x = Gx*(dT) + ang_x_prev
			ang_y = Gy*(dT) + ang_y_prev
			ang_z = Gz*(dT) + ang_z_prev
			
			ang_x_prev = ang_x
			ang_y_prev = ang_y
			ang_z_prev = ang_z
		
#============================== MPU6050_Distancia ===============================
		#if abs(vel)>0.002: 
		vel = Ax*(dT*100) + vel_prev
		vel_prev = vel
	
		dist = dist_prev + vel*(dT*100) + 0.5*Ax*pow((dT*10),2)
		dist_prev = dist
			
		tempo_f= time.time()
		dT = tempo_f - tempo_i
#================================================================================
		cont+=1
		if cont == 25:
			cont = 0
			x = 48-(ang_z*18)
			#Prints:
			#print("AccZangle=%.2f" %AccZangle, u'\u00b0'+ "/s")
			#print("o tempo utilizado foi %.5f s" %dT)
			#print("Gz: %.2f" %Gz)
			print("Rotacao em Z: %.2f" %(ang_z*8))
			print("potencia do motor: %.2f" %x)
			#print("---------------------------------")
			#print("Aceleracao = %.2f" %Ax)
			#print("Velocidade = %.2f" %vel)
			#print("o tempo utilizado foi %.5f s" %dT)
			print("Distancia = %.2f" %(dist*28/(1000*30)))
			print("---------------------------------")
		if (ang_z*8) < -2:
			#motorA_pwm.ChangeDutyCycle() #~5V
			motorB_pwm.ChangeDutyCycle(int(83-(ang_z*12))) #~5V
		elif (ang_z*8) > 2:
			#motorA_pwm.ChangeDutyCycle(40) #~5V
			motorB_pwm.ChangeDutyCycle(int(83-(ang_z*8))) #~5V
		if (dist*28/(1000*30) >2.9):
			break
			

#================================== MPU6050_spin =========================================
def mpu6050_spin():
	print (" Reading Data of Gyroscope and Accelerometer")
	cont = 0
	ang_x_prev = 0
	ang_y_prev = 0
	ang_z_prev = 0
	ang_x = 0
	ang_y = 0
	ang_z = 0
	tempo_i = 0
	tempo_f = 0
	dT = 0
	x = 0
	
	while True:
		tempo_i = time.time() #contar tempo do loop
		
		#Read Gyroscope raw value
		gyro_x = read_raw_data(GYRO_XOUT_H)
		gyro_y = read_raw_data(GYRO_YOUT_H)
		gyro_z = read_raw_data(GYRO_ZOUT_H)	
		
		Gx = gyro_x/131.0 #32768/250
		Gy = gyro_y/131.0 #32768/250
		Gz = gyro_z/131.0 #32768/250
		
		
#============================== MPU6050_Angulo ==================================
		if abs(Gz)>0.2:		
			#Calculo do angulo de rotacao
			ang_x = Gx*(dT) + ang_x_prev
			ang_y = Gy*(dT) + ang_y_prev
			ang_z = Gz*(dT) + ang_z_prev
			
			ang_x_prev = ang_x
			ang_y_prev = ang_y
			ang_z_prev = ang_z
			
		tempo_f= time.time()
		dT = tempo_f - tempo_i
#================================================================================
		cont+=1
		if cont == 50:
			cont = 0
			#Prints:
			#print("AccZangle=%.2f" %AccZangle, u'\u00b0'+ "/s")
			print("o tempo utilizado foi %.5f s" %dT)
			print("Gz: %.2f" %Gz)
			print("Rotacao em Z: %.2f" %(ang_z*8))
			print("---------------------------------")
			
		if abs(ang_z*8) > 165:
				print("Deu 180 graus")
				break
	
try:     
	anda_irriga()
	#while True:        
	#	direction = input('(a-anda e irriga, f-forward, s-spin, r-reverse): ')
	#	
	#	if direction[0] == 's':
	#		spin()
	#	elif direction[0] == 'f':
	#		forward()
	#	elif direction[0] == 'r':
	#		reverse()
	#	elif direction[0] == 'a':
	#		anda_irriga()
finally:  
    print("Cleaning up")
    GPIO.cleanup()
