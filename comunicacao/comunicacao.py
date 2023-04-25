#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import serial
import keyboard

# [!!] PARA RODAR NO LINUX:
aport = serial.Serial('/dev/ttyACM0', 9600, timeout=1, dsrdtr=True)

# Get a reference to webcam #0 (the default one)
# Para corrigir o problema do loop, dsrdtr foi configurada como True:
### dsrdtr (bool) – Enable hardware (DSR/DTR) flow control.
# aport = serial.Serial("COM3", 9600, timeout=1, dsrdtr=True)

# Função temporária apenas para a prova de conceito que registra
# os dígitos de 1-4 quando pressionados no teclado, representando os quadrantes.
# Mais tarde, uma função enviará esses mesmos dígitos, mas em vez de vir do teclado,
# virão do reconhecimento facial.
def identif_quad() -> int:
    kb = keyboard.read_key()
    while kb!='1' and kb!='2' and kb!='3' and kb!='4':
        kb = keyboard.read_key()
    return int(kb)

# Loop que envia os quadrantes identificados ao Arduino.
while aport:
    quadrante = identif_quad()
    quadrante = quadrante.to_bytes(2,"big")
    print(f"{quadrante} e {type(quadrante)}") #para testes
    aport.write(quadrante)
    
