# [!!] Ultra RASCUNHO quanto a integração de facereg.py e comunicacao.py [!!]
# eu só estava testando a integração no caso então limpei todos os comentários, meus ou do código que peguei na documentação do face_recognition
# os códigos originais (que essa está juntando) estão com todos intactos ainda

import serial
import face_recognition
import numpy as np
import cv2

#aport = serial.Serial('/dev/ttyUSB0', 9600)
video_capture = cv2.VideoCapture(0)
face_locations = []
face_encodings = []
process_this_frame = True

def identif_quad(video_capture, face_locations, face_encodings, process_this_frame):
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

while True:
    quadrante = bytes(identif_quad(video_capture, face_locations, face_encodings, process_this_frame))
    print(quadrante)
    #aport.write(quadrante)
    #aport.read()
    
# [!!] Mesmo como print  atualmente não roda [!!]
# TypeError: 'tuple' object cannot be interpreted as an integer
