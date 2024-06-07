import sys
import os
import pyautogui
from time import sleep
from customtkinter import *
from subprocess import Popen
from threading import Thread

working = True

# Interface do usuário
def interface():
    janela = CTk()
    janela.title("Automação Netflix")
    janela.geometry("500x350")

    fonte = CTkFont(size=14)
    label = CTkLabel(janela, text="Selecione o que deseja pular: ", font=fonte)
    label.grid(column=0, row=0, padx=20, pady=(10, 0), sticky="w")

    janela.grid_columnconfigure(0, weight=1)
    janela.grid_columnconfigure(1, weight=1)

    pular_resumo_var = IntVar()
    pular_abertura_var = IntVar()
    pular_episodio_var = IntVar()

    check_pular_r = CTkCheckBox(janela, text="Pular Resumo", variable=pular_resumo_var, onvalue=1, offvalue=0, corner_radius=36)
    check_pular_r.grid(column=0, row=1, padx=20, pady=(10, 0), sticky="w")

    check_pular_a = CTkCheckBox(janela, text="Pular Abertura", variable=pular_abertura_var, onvalue=1, offvalue=0, corner_radius=36)
    check_pular_a.grid(column=0, row=2, padx=20, pady=(10, 0), sticky="w")

    check_pular_e = CTkCheckBox(janela, text="Próximo Episódio", variable=pular_episodio_var, onvalue=1, offvalue=0, corner_radius=36)
    check_pular_e.grid(column=0, row=3, padx=20, pady=(10, 0), sticky="w")

    botao_netflix_executar = CTkButton(janela, text="Abrir Netflix e Executar", command=lambda: abrir_netflix_sp(pular_resumo_var, pular_abertura_var, pular_episodio_var))
    botao_netflix_executar.grid(column=0, row=4, padx=20, pady=20, columnspan=2, sticky="w")

    botao_netflix = CTkButton(janela, text="Executar", command=lambda: executar_pular(pular_resumo_var, pular_abertura_var, pular_episodio_var))
    botao_netflix.grid(column=1, row=4, padx=20, pady=20, columnspan=2, sticky="e")

    botao_reiniciar = CTkButton(janela, text="Reiniciar", command=reiniciar)
    botao_reiniciar.grid(column=0, row=5, padx=20, pady=20, columnspan=2, sticky="ew")

    botao_sair = CTkButton(janela, text="Sair", command=lambda: sair(janela))
    botao_sair.grid(column=0, row=6, padx=20, pady=20, columnspan=2, sticky="ew")
    
    janela.mainloop()

# Abre o Netflix(Botão)
def abrir_netflix_sp(a, b, c):
    # Popen abre o site do netflix no chrome e na proxima linha a função executar_pular() é chamada
    Popen(["start", "chrome", "netflix.com"], shell=True)
    executar_pular(a, b, c)

# Abre a função pular()(Botão)
def executar_pular(a, b, c):
    # Thread permite que o programa seja executado em segundo plano, deixando a interface livre para a interação com o usuário.
    Thread(target=pular, args=(a.get(), b.get(), c.get())).start()

# Reinicia o programa(Botão)
def reiniciar():
    python = sys.executable
    os.execl(python, python, *sys.argv) 

# Sai do Programa(Botão)
def sair(janela):
    global working
    working = False
    janela.destroy()
    sys.exit()

# Função que executa a tarefa principal: pular os resumos, aberturas e seguir para o próximo episódio automaticamente.
def pular(pular_resumo_var, pular_abertura_var, pular_episodio_var):
    global working
    while working:
        # Pular resumo (chamada no checkbox da interface)
        try:
            if pular_resumo_var:
                pular = pyautogui.locateOnScreen("images/pular.png", confidence=0.7, region=(1404, 688, 600, 800))
                if pular is not None:
                    pyautogui.moveTo(pular)
                    pyautogui.click(pular)
                    sleep(1)
                else:
                    print("pular")
        except Exception as e:
            print(e, "a")
        # Pular abertura (chamada no checkbox da interface)    
        try:
            if pular_abertura_var:
                abertura = pyautogui.locateOnScreen("images/abertura.png", confidence=0.7, region=(1404, 688, 600, 800))
                if abertura is not None:
                    pyautogui.moveTo(abertura)
                    pyautogui.click(abertura)
                    sleep(1)
                else:
                    print("pular")
        except Exception as e:
            print(e, "b")
        # Pular episódio (chamada no checkbox da interface)        
        try:
            if pular_episodio_var:
                proximo = pyautogui.locateOnScreen("images/proximo.png", confidence=0.7, region=(1404, 688, 600, 800))    
                if proximo is not None:
                    pyautogui.moveTo(proximo)
                    pyautogui.click(proximo)
                    sleep(1)
                else:
                    ("proximo")
        except Exception as e:
            print(e, "c")
        sleep(0.5)
    pass


if __name__ == "__main__":
    interface()

