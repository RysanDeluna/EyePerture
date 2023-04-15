#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import serial
import keyboard

aport = serial.Serial("COM3", 9600, timeout=1, dsrdtr=True)

def identif_quad() -> int:
    kb = keyboard.read_key()
    while kb!='1' and kb!='2' and kb!='3' and kb!='4': # não modifiquei para o que a gente 
        kb = keyboard.read_key()                       # fez em sala pois poderia gerar outros problemas
    # futuramente ira retornar o quadrante
    # do rosto, identificado com o uso de APIs
    return int(kb)

while aport:
    quadrante = bytes(identif_quad())
    #print(quadrante)
    aport.write(quadrante)
    aport.read()
