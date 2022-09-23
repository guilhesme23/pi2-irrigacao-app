import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# escolha dos pinos
enableA_pin = 29    
in_1_pin = 31
in_2_pin = 33

enableB_pin = 22
in_3_pin = 12
in_4_pin = 16
#Definicao dos pinos como saida
GPIO.setup(enableA_pin, GPIO.OUT)
GPIO.setup(in_1_pin, GPIO.OUT)
GPIO.setup(in_2_pin, GPIO.OUT)

GPIO.setup(enableB_pin, GPIO.OUT)
GPIO.setup(in_3_pin, GPIO.OUT)
GPIO.setup(in_4_pin, GPIO.OUT)

#Habilita o PWM com uma frequência de 300Hz
motorA_pwm = GPIO.PWM(enableA_pin, 300)
motorB_pwm = GPIO.PWM(enableB_pin, 300)

#Liga os dois motores 
motorA_pwm.start(0)
motorB_pwm.start(0)

cont = 0

#Função para andar para frente
def forward():          
    GPIO.output(in_2_pin, True) 
    GPIO.output(in_1_pin, False) 
    GPIO.output(in_4_pin, True) 
    GPIO.output(in_3_pin, False)     
    motorA_pwm.ChangeDutyCycle(40) #Esquerdo
    motorB_pwm.ChangeDutyCycle(55) #Direito
    time.sleep(5)
    motorA_pwm.ChangeDutyCycle(0)
    motorB_pwm.ChangeDutyCycle(0)    
    
#Função para andar para trás
def reverse():          
	GPIO.output(in_2_pin, False) 
	GPIO.output(in_1_pin, True) 
	GPIO.output(in_4_pin, False) 
	GPIO.output(in_3_pin, True)     
	motorA_pwm.ChangeDutyCycle(60) #~5V
	motorB_pwm.ChangeDutyCycle(60) #~5V
	time.sleep(3)
	motorA_pwm.ChangeDutyCycle(0)
	motorB_pwm.ChangeDutyCycle(0) 

#Função para girar
def spin():          
	GPIO.output(in_1_pin, False) 
	GPIO.output(in_2_pin, True) 
	GPIO.output(in_3_pin, True) 
	GPIO.output(in_4_pin, False)  
	motorA_pwm.ChangeDutyCycle(60)
	motorB_pwm.ChangeDutyCycle(60)
	time.sleep(4) 
	motorA_pwm.ChangeDutyCycle(0)
	motorB_pwm.ChangeDutyCycle(0)
     
#Função para parar 
def stop():
    GPIO.output(in_1_pin, False) 
    GPIO.output(in_2_pin, False) 
    motorA_pwm.ChangeDutyCycle(0)
    motorB_pwm.ChangeDutyCycle(0)
    
try:         
    while True:        
        direction = input('Enter direction letter (f-forward, s-spin, r-reverse): ')
        if direction[0] == 'r':
            reverse()
        elif direction[0] == 'f':
            forward()
        elif direction[0] == 's':
            spin()
        
finally:  
    print("Cleaning up")
    GPIO.cleanup()
