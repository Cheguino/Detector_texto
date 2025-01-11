import cv2 #procesamiento de imágenes
import easyocr # detectar texto en imágenes
import matplotlib.pyplot as plt  
import numpy as np

# ruta de la imagen que se quiere analizar.
image_path = 'C:\\Users\\L\\Desktop\\data\\test1.png'

img = cv2.imread(image_path) #Carga la imagen desde la ruta

# Indica que se buscará texto en inglés
reader = easyocr.Reader(['en'], gpu=False)

#  detecta tecto en la imagen
text_ = reader.readtext(img)

#umbral de confianza para filtrar las detecciones menos confiables
#Solo se procesarán las detecciones cuyo score sea mayor a este valor
threshold = 0.25

#
for t_, t in enumerate(text_):
    print(t)

    bbox, text, score = t

    if score > threshold:
        #Dibuja un rectángulo verde alrededor del texto detectado.
        cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)
        #Escribe el texto detectado
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (0, 0, 0), 2)

#Muestra la imagen procesadax
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
