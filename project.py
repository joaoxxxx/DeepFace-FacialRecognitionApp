from deepface import DeepFace
import cv2
import os
from tkinter import simpledialog, Tk, Button, Label
from threading import Thread
import time
import win32gui
import win32con


class FacialRecognitionApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Reconhecimento Facial com DeepFace")
        self.root.geometry("300x200")
        self.root.iconbitmap("icon.ico")
        self.root.configure(bg='#f0f0f0')

        self.captura_status = False
        self.status_label = None
        self.create_ui()

    def create_ui(self):
        Button(self.root, 
            text="Iniciar Captura", 
            command=self.start_capture,
            bg='#4CAF50',
            fg='white',
            relief='raised',
            padx=10).pack(pady=10)

        Label(self.root, 
            text="Pressione 'Iniciar Captura' para começar\nPressione 'Esc' para sair",
            bg='#f0f0f0',
            fg='#333333').pack(pady=10)

        Button(self.root, 
            text="Iniciar Reconhecimento (DeepFace)", 
            command=self.start_recognition,
            bg='#2196F3',
            fg='white',
            relief='raised',
            padx=10).pack(pady=10)

        self.status_label = Label(self.root, 
            text="",
            bg='#f0f0f0',
            fg='#333333')
        self.status_label.pack(pady=5)

    def start_capture(self):
        self.captura_status = True
        capture_thread = Thread(target=self.capture_frames)
        capture_thread.start()

    def ask_user_name(self, frame, img_counter):
        user_name = simpledialog.askstring("Input", "Nome:", parent=self.root)
        if user_name:
            sanitized_name = "".join(c for c in user_name if c.isalnum())
            os.makedirs("db", exist_ok=True)
            img_name = f"db/{sanitized_name}_{img_counter}.png"
            if frame is not None:
                cv2.imwrite(img_name, frame)
                print(f"{img_name} salvo!")
            else:
                print("Frame inválido. Não foi possível salvar.")

    def capture_frames(self):
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("Captura")
        img_counter = 0
        prev_time = time.time()
        
        hwnd = win32gui.FindWindow(None, "Captura")
        icon = win32gui.LoadImage(
            0, "icon.ico", win32con.IMAGE_ICON,
            0, 0, win32con.LR_LOADFROMFILE
        )
        if hwnd:
            win32gui.SendMessage(
                hwnd, win32con.WM_SETICON,
                win32con.ICON_SMALL, icon
            )
            win32gui.SendMessage(
                hwnd, win32con.WM_SETICON,
                win32con.ICON_BIG, icon
            )
        
        try:
            while self.captura_status:
                ret, frame = cam.read()
                if not ret:
                    print("Falha ao capturar frame")
                    break


                current_time = time.time()
                fps = 1 / (current_time - prev_time)
                prev_time = current_time

                cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                    1, (0, 255, 0), 2, cv2.LINE_AA)
                            
                cv2.imshow("Captura", frame)
                key = cv2.waitKey(1)
                if key % 256 == 27:  # ESC
                    print("Encerrando captura")
                    self.captura_status = False
                    break
                elif key % 256 == 32:  # espaço
                    self.root.after(0, self.ask_user_name, frame.copy(), img_counter)
                    img_counter += 1
        finally:
            cam.release()
            cv2.destroyAllWindows()

    def start_recognition(self):
        self.status_label.config(text="Reconhecimento em andamento...", fg="green")
        recognition_thread = Thread(target=self.run_deepface)
        recognition_thread.start()

    def run_deepface(self):
        try:
            print("Iniciando reconhecimento facial com DeepFace...")
            DeepFace.stream("db", model_name="VGG-Face",enable_face_analysis=True)
        except Exception as e:
            print(f"Erro durante reconhecimento: {e}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = FacialRecognitionApp()
    app.run()
