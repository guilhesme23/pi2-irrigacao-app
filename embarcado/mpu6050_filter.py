import smbus		#import SMBus module of I2C
import time
from math import atan2
from math import pow
from math import sqrt

#Peso do giroscopio no filtro complementar
peso_giro = 0.98 
const_gravid = 9.81

#Variaveis de tempo
tempo_i = 0
tempo_f = 0
dT = 0
cont = 0

#inicalizacao de variaveis de angulo:
gyroXangle = 0
gyroYangle = 0
gyroZangle = 0
CFangleX = 0
CFangleY = 0
CFangleZ = 0
ang_x_prev = 0
ang_y_prev = 0
ang_z_prev = 0
ang_z = 0

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

bus = smbus.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address

MPU_Init()

print (" Reading Data of Gyroscope and Accelerometer")

while True:
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
	AccXangle = (atan2(acc_x, sqrt(pow(acc_y,2) + pow(acc_z,2)))*180)/3.14;
	AccYangle = (atan2(acc_y, sqrt(pow(acc_x,2) + pow(acc_z,2)))*180)/3.14;
	AccZangle = (atan2(acc_z, sqrt(pow(acc_x,2) + pow(acc_y,2)))*180)/3.14;
	
	#Calcula a distância percorrida por integração simples
	#com base no tempo de loop (dT = tempo_f - tempo_i)
	gyroXangle+=Gx*dT;
	gyroYangle+=Gy*dT;
	gyroZangle+=Gz*dT;
	
	#Fusão dos dados: giro + accel
	#Método: filtro complementar:
	#Atribui peso de 0.98 ao valor do giro e 0.02 ao acelerometro
	CFangleX=peso_giro*(CFangleX+Gx*(dT/1000))+(1-peso_giro) * AccXangle;
	CFangleY=peso_giro*(CFangleY+Gy*(dT/1000))+(1-peso_giro) * AccYangle;
	CFangleZ=peso_giro*(CFangleZ+Gz*(dT/1000))+(1-peso_giro) * AccZangle;
	
	if abs(Gz)>0.2:		
		#Calculo do angulo de rotacao
		ang_x = Gx*(dT/1000) + ang_x_prev
		ang_y = Gy*(dT/1000) + ang_y_prev
		ang_z = Gz*(dT) + ang_z_prev
		
		ang_x_prev = ang_x
		ang_y_prev = ang_y
		ang_z_prev = ang_z

	
	tempo_f= time.time()
	dT = tempo_f - tempo_i
	
	
	a = Gz*dT/1000
	cont+=1
	if cont == 125:
		cont = 0
		#Prints:
		#print("AccZangle=%.2f" %AccZangle, u'\u00b0'+ "/s")
		print("o tempo utilizado foi %.5f s" %dT)
		print("Gz: %.2f" %Gz)
		print("Rotacao em Z: %.2f" %(ang_z*8))

		print("---------------------------------")
	
	
	#time.sleep(dT)
