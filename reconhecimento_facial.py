import face_recognition
import numpy as np
import cv2
import serial

def encontra_rosto(video_capture, PROCESS_FRAME):
    face_locations = []
    ret, frame = video_capture.read()
    if PROCESS_FRAME == True:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        
        face_locations = face_recognition.face_locations(rgb_small_frame)
    PROCESS_FRAME = not PROCESS_FRAME
    
    # Mostra a imagem de vídeo com um retângulo --> Testing only!
    for (top, right, bottom, left) in face_locations:
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0,0,255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0,0,255), cv2.FILLED)
    
    cv2.imshow('Video', frame)
    try:
        return face_locations, PROCESS_FRAME, small_frame.shape
    except:
        return face_locations, PROCESS_FRAME, 0

def identifica_quadrantes(face_locations):
    try:
        top, right, bottom, left = face_locations[0] 
        #print(top, right, bottom, left)
    except:
        return ''
    if top <= 40 and right < 100:
        return 1
    elif top <= 40 and right >= 100:
        return 2
    elif top > 40 and right >= 100:
        return 3
    elif top > 40 and right < 100:
        return 4
    
if __name__ == "__main__":
    aport = serial.Serial('/dev/ttyACM0', 9600, timeout=1, dsrdtr=True)
    video_capture = cv2.VideoCapture(0)
    PROCESS_FRAME = True

    while True: 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        face_locations, PROCESS_FRAME, shape = encontra_rosto(video_capture, PROCESS_FRAME)
        quad = bytes(str(identifica_quadrantes(face_locations)), "utf-8")
        #quad = identifica_quadrantes(face_locations)
        print(quad)
        aport.write(quad)
 
    video_capture.release()
    cv2.destroyAllWindows()
