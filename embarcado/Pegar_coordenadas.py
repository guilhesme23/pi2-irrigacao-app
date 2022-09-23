#!/usr/bin/env python
import requests
import os
#função que retorna se o usuário solicitou ou não começar a irrigar, True ou False:
def inicializacaoUsuario():
    r = requests.get('http://ec2-3-80-149-132.compute-1.amazonaws.com:5000/commands/irrigate')
    resposta = r.json()
    resposta = resposta['data']    
    return resposta

#função que retorna o mapa
def pegarCoordenadas():
    r = requests.get('http://ec2-3-80-149-132.compute-1.amazonaws.com:5000/trajectory/')
    coordenadas = r.json()
    coordenadas = coordenadas['route']['irrigation_route']['irrigation_route']
    return coordenadas

if inicializacaoUsuario():
    coordenadas = pegarCoordenadas()
    print(coordenadas)
    os.system("python3 exe_PI2")




