#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import serial
import keyboard # (por enquanto)

aport = serial.Serial('/dev/ttyUSB0', 9600)

def identif_quad() -> int:
    kb = keyboard.read_key()
    while kb!='1' and kb!='2' and kb!='3' and kb!='4':
        kb = keyboard.read_key()
    # futuramente ira retornar o quadrante
    # do rosto, identificado com o uso de APIs
    return int(kb) # PLACEHOLDER

while aport:
    quadrante = bytes(identif_quad())
    aport.write(quadrante)
    aport.read()
