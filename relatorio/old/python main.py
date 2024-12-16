from deepface import DeepFace
import cv2
import numpy as np
from tkinter import simpledialog, Tk, Button, Label
import threading

root = Tk()
root.title("Reconhecimento Facial com DeepFace")
root.geometry("300x200")

captura_status = False

def captura():
    global captura_status
    captura_status = True
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Captura")
    img_counter = 0
    
    while captura_status:
        ret, frame = cam.read()
        if not ret:
            print("Falha ao capturar frame")
            break
        cv2.imshow("Captura", frame)

        k = cv2.waitKey(1)
        if k % 256 == 27:  # esq sair
            print("Encerrando captura")
            captura_status = False 
            break
        elif k % 256 == 32:  #space
            user_name = simpledialog.askstring("Input", "Nome:", parent=root)
            if user_name:
                img_name = f"db/{user_name}{img_counter}.png"
                cv2.imwrite(img_name, frame)
                print(f"{img_name} escrito!")
                img_counter += 1

    cam.release()
    cv2.destroyAllWindows()

    

def analise_deepface():
    global captura_ativa
    captura_ativa = False 
    DeepFace.stream("db", model_name="VGG-Face")

capture_button = Button(root, text="Iniciar Captura", command=captura)
capture_button.pack(pady=10)

info_label = Label(root, text="Pressione 'Iniciar Captura' para começar\nPressione 'Esc' para sair")
info_label.pack(pady=10)

deepface_button = Button(root, text="Iniciar Reconhecimento (DeepFace)", command=analise_deepface)
deepface_button.pack(pady=10)

root.mainloop()
