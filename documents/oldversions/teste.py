import sys
from tkinter import Tk, Label, Button
from io import StringIO

# Função para capturar saída e atualizar Label
def capture_output():
    # Redireciona sys.stdout para um StringIO
    sys.stdout = StringIO()
    
    # Exemplo de saída para redirecionar
    print("Este é um exemplo de saída!")
    
    # Captura o valor de sys.stdout e exibe no Label
    output_text = sys.stdout.getvalue()
    osoutput.config(text=output_text)

    # Restaura o stdout original
    sys.stdout = original_stdout

# Configuração da janela Tkinter
root = Tk()
root.title("Captura de Saída no Tkinter")
root.geometry("300x200")

# Salva o stdout original
original_stdout = sys.stdout

# Cria o Label para exibir a saída
osoutput = Label(root, text="")
osoutput.pack(pady=10)

# Botão para capturar e exibir a saída
output_button = Button(root, text="Mostrar Saída", command=capture_output)
output_button.pack(pady=10)

# Mantém a janela do Tkinter aberta
root.mainloop()
