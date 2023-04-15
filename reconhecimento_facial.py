import face_recognition
import numpy as np
import cv2

# [!!] Esse código vai para o comunicacao.py eventualmente, mas enquanto não se resolve o problema do serial quero deixar aqui [!!]
# para evitar que fique MUITO bagunçado e para tudo ser resolvido passo a passo em vez de ficar caótico

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)
# Initialize some variables
face_locations = []
face_encodings = []
process_this_frame = True

# Função que identifica as localizações do rosto que está sendo capturado pela webcam no momento
# e as devolve dentro uma tupla. Dentro dela, faz algumas coisas para reduzir o tempo de processamento da imagem.
def pega_localizacoes(video_capture, face_locations, face_encodings, process_this_frame):
    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()
        # Only process every other frame of video to save time
        if process_this_frame:
             # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        process_this_frame = not process_this_frame
        # Normalmente o for seguinte na função que usei como referência faria o isso:
        ### Display the results (não é relevante para o nosso caso)
        # Entretanto, no momento está contido nela o return da função.
        # [!!] Eu sei e concordo que não faz sentido o return aqui, mas por *algum* motivo buga se tento fora dele,
        # então, *por enquanto* fica aqui mesmo.
        for (top, right, bottom, left) in face_locations:
            return(face_locations)
    # Para o nosso projeto não é relevante, mas deixei para evitar chance do código quebrar
    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()

while True:  
  print(pega_localizacoes(video_capture, face_locations, face_encodings, process_this_frame)) #print para teste

# [!!] No momento está ok, mas dependendo de como é feito o código, a leitura dos quadrantes fica lenta
# [!!] Eu removi enquanto limpando esse código, mas caso necessário para a prova de conceito posso colocar de novo
# um trecho do código que mostra a imagem sendo capturada e opcionalmente um frame em volta do rosto detectado.
# Minhas referências:
### https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py
### https://face-recognition.readthedocs.io/en/latest/face_recognition.html
# face-recognition package: https://pypi.org/project/opencv-python/      [ pip install opencv-python    ]
# opencv:                   https://pypi.org/project/face-recognition/   [ pip install face-recognition ]
