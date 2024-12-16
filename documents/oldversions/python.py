
##usar python 3.12 ---- deepface e tensorflow nao suportam 3.13"""

## objetivos: ao abrir o programa tira 1 foto e guardar na DB (outra a cada 30 segundos);; deepface stream detects ;; quando uma cara for identificada da Database adicionar a um ficheiro txt as entradas registadas

## CAPTURAR FRAMES HA INTERFERENCIA POR JA EXISTEREM FOTOS COM O MESMO NOME, talvez inves de dar nome dar um numero random ou ler de pasta ou de ficheiro .txt os que ainda nao existem

from deepface import DeepFace
import matplotlib.pyplot as plt
import cv2
import numpy as np
from tkinter import simpledialog, Tk ### VER TKINTER 
import tkinter

root = Tk() #VER ROOT
root.withdraw()

cam = cv2.VideoCapture(0)
cv2.namedWindow("Captura")
img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed toframe")
        break
    cv2.imshow("Captura", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        print("closing")
        break
    elif k%256 == 32: # ASCII para space bar
        user_name = simpledialog.askstring("Input", "Nome:", parent=root)
        if user_name:
            img_name = f"db/{user_name}{img_counter}.png"
            cv2.imwrite(img_name, frame)
            print(f"{img_name} written!")
            img_counter += 1

cam.release()
cv2.destroyAllWindows()

DeepFace.stream("db", model_name = "VGG-Face") ############### VGG É MAIS RAPIDO
