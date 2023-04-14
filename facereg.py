#import serial
import face_recognition
import numpy as np
import cv2

# [!!] Esse código vai para o comunicacao.py eventualmente, mas enquanto não se resolve o problema do serial quero deixar aqui [!!]
# para evitar que fique MUITO bagunçado e para tudo ser resolvido passo a passo em vez de ficar caótico

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
            # [!!] eu sei que não faz sentido o return aqui, mas por *algum* motivo buga se tento fora desse for [!!]
            return(face_locations)
            # vv não sei se é relevante no nosso caso
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            #top *= 4
            #right *= 4
            #bottom *= 4
            #left *= 4
    # vv acho que não é relevante, mas deixei para evitar chance do código quebrar
    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()

while True:
  # print é só para testes, eu juntar comunicacao.py com esse faço a integração certinha
  # [!!] dependendo de como é feito, a leitura dos quadrantes fica EXTREMAMENTE lenta [!!]
  # esse jeito do código ainda está numa velocidade ok porém
  print(pega_localizacoes(video_capture, face_locations, face_encodings, process_this_frame))

# [!!] Eu removi enquanto limpando esse código, mas caso necessário para a prova de conceito posso colocar de novo
# um trecho do código que mostra a imagem sendo capturada e opcionalmente um frame em volta do rosto detectado [!!]
