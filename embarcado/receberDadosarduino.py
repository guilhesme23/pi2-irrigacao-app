# Código para pegar os dados dos sensores do arduino via rádio e enviar para o servidor web.
import piVirtualWire.piVirtualWire as piVirtualWire
# Necessário importar a lib pigpio também, pois a piVirtualWire utiliza ela para se comunicar
import time, pigpio
import requests
import json

pi = pigpio.pi()

RX = 27
BPS = 2000
# Primeiro parâmetro é a instância do pigpio.
# Segundo é a porta do GPIO que irá utilizar.
# Terceiro é a taxa de comunicação, mesmo que o transmissor
# Note que aqui é utilizado o método rx e não tx como no transmissor
rx = piVirtualWire.rx(pi, RX, BPS)
cont = 0
while True:
    # loop infinito escutando tudo assim que conseguir alguma coisa ele imprime.
    while rx.ready():
        # o rx.get() retorna um array com códigos da tabela ASCII (http://www.asciitable.com/)
        # então é necessário converter para ter a mensagem correta.
        #print("Dentro do looping rxready")
                #print("ANYTHING")

        msg = ''.join(chr(i) for i in rx.get())
        msg = int(msg)
        if msg == 1111:
            cont = cont+1
            print('cont1')
        elif cont == 1:
            h_s = msg
            cont=cont+1
            print('cont2')
        elif cont == 2:
            print('cont3')
            h_a = msg
            cont = cont+1
        elif cont == 3:
            print('cont4')
            t_a = msg
            cont = cont+1
        if msg == 2222:
            dados_sensores = {"temp_air":t_a, "temp_soil":20, "humidity_air":h_a, "humidity_soil":h_s}
            print(dados_sensores)
            r = requests.post("http://ec2-3-80-149-132.compute-1.amazonaws.com:5000/sensors", data=json.dumps(dados_sensores))
            print(r)
            print(r.json())
        print(msg)
    #print("Aguardando...")
    time.sleep(0.5)

rx.cancel()
pi.stop()            
