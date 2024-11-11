# Bot WhatsApp, envio de mensagem em massa

## Bibliotecas
import pyautogui
import webbrowser
from time import sleep

## Código

# Lista dos contatos
contatos = [5594992238197, 5594981197102]

# Laço de repetição
for telefone in contatos:
    webbrowser.open(f'http://api.whatsapp.com/send?phone={telefone}')
    sleep(20)
