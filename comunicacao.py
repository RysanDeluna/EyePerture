#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import serial
import keyboard
# import time (5) //adiciona esse import

aport = serial.Serial('/dev/ttyUSB0', 9600)
# (3) //adiciona seguinte linha
# aport.setTimeout(1)

# (4)
# //adiciona seguinte linha
# aport.dtr=True
# OU
# //substitui por seguinte linha
# aport = serial.Serial('/dev/ttyUSB0', 9600, timeout=None, dsrdtr=True)
# OU
# //substitui por seguinte linha
# arduino = serial.Serial(port='COM4', baudrate=115200, timeout=None, dsrdtr=True, rtscts=True)

def identif_quad() -> int:
    kb = keyboard.read_key()
    while kb!='1' and kb!='2' and kb!='3' and kb!='4': # não modifiquei para o que a gente 
        kb = keyboard.read_key()                       # fez em sala pois poderia gerar outros problemas
    # futuramente ira retornar o quadrante
    # do rosto, identificado com o uso de APIs
    return int(kb) # PLACEHOLDER

# (1) //substitui seguinhte linha
# while (aport.available()):
# OU
# while (aport.avaiable()>0):
while aport:
    quadrante = bytes(identif_quad())
    aport.write(quadrante)
    aport.read()
    # (2) //adiciona seguinte linha(s)
    # aport.flush()
    # aport.flushInput()
    # aport.flushOutput()

    # (5) //adiciona seguinte linha
    # time.sleep(0.5)


# ==== 1 ====
# usar .available() no loop, pelo que entendi no próprio while e ok

# ==== 2 ====
# uso de .flush() ao fim do loop
# não sei se os de input/output são necessários, só segui o que achei

# ==== 3 ====
# uso do timeout

# ==== 4 ====
# não entendi 100% o que seria o dsrdtr, mas é algo em relação a ports e resetar o arduino
# quanto ao rtscts, é usado nesse seguinte caso:
# "counterpart for clone boards that still use RTS to auto reset, add even RTS."
# acho que teoricamente o timeout poderia ser timeout=1

# ==== 5 ====
# uso da função .sleep()

# ==== 6 ====
# nào coloquei nada porque não acho que se aplica ao nosso?
# mas li algo sobre a baudrate que estamos empregando (9600) ser lenta
# mas de novo, não acho que se aplica e passei por vários códigos mantendo o 9600

# ==== 7 ====
# https://forum.arduino.cc/t/pc-arduino-comms-using-python-updated/574496
# olhei muito rápido e não achei que se aplica? mas vai que

# ==== 8 ====
# passei por alguns usando while 1 no lugar do nosso "while aport" atual, mas creio que dê na mesma
