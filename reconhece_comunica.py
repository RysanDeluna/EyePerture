# [!!] Ultra RASCUNHO quanto a integração de facereg.py e comunicacao.py [!!]
# Eu só estava testando a integração no caso então limpei todos os comentários, meus ou do código que peguei na documentação do face_recognition
# os códigos originais (que essa está juntando) estão com todos intactos ainda, então por enquanto NÃO use esse como referência

import serial
import face_recognition
import numpy as np
import cv2

#aport = serial.Serial('/dev/ttyUSB0', 9600)
video_capture = cv2.VideoCapture(0)
face_locations = []
face_encodings = []
process_this_frame = True

def pega_localizacoes(video_capture, face_locations, face_encodings, process_this_frame):
    while True:
        ret, frame = video_capture.read()
        if process_this_frame:
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        process_this_frame = not process_this_frame
        for (top, right, bottom, left) in face_locations:
            return(face_locations)
    video_capture.release()
    cv2.destroyAllWindows()

# Alguma função (ou outra coisa, só estou marcando por organizacão) que converta as localizações contidas na tupla
# em seu quadrante equivalente adequado
def identif_quadrantes(face_locations):
    quadrante = face_locations
    # [...] - Trecho do código que converte adequadamente para o quadrante correspondente, que será um valor de 1-4
    # O número '0' é só um placeholder.
    quadrante = 0
    return quadrante

while True:
    # Pega as localizações da face
    local_face = pega_localizacoes(video_capture, face_locations, face_encodings, process_this_frame)
    # Passa para o quadrante adequado e converte para byte
    quadrante = bytes(str(identif_quad(local_face)),"utf-8")
    print(quadrante) # Para testes
    # Envia ao Arduino
    aport.write(quadrante)
    aport.read()

# [!!] Não testei NADA disso, é só um rascunho~planejamento.
