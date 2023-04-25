# EyePerture

<img href="https://user-images.githubusercontent.com/100282290/234154652-4e1b5124-5599-41d6-94aa-b06c2ee570d7.png" height="400"/>

* `ard.c`: código do arduino
* `comunicacao.py`: código da comunicação entre Arduino e código Python
  * Futuramente, reconhecimento_facial.py estará dentro dessa função
* `reconhecimento_facial.py`: código do reconhecimento facial e que pega as localizações do rosto [TEMP]
* `reconhece_comunica.py`: código rascunho  da integração entre comunicacao.py e reconhecimento_facial.py [TEMP]

---

**Em relação ao reconhecimento_facial.py:**
* Para rodar:
  * Instalar o [dlib](http://dlib.net); [guia para Linux](https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf) 
  * Instalação para Windows: [guia](https://github.com/ageitgey/face_recognition/issues/175#issue-257710508)
  * pip install opencv-python
  * pip install face_recognition
* Retorna a tupla face_locations, que, por sua vez, tem o valor [top, right, bottom, left]
* [Vídeo de como o código retorna no Windows corretamente configurado](https://www.youtube.com/watch?v=aURCHOb-zgo)
