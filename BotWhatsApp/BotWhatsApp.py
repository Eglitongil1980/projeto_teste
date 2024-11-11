# Bot WhatsApp, envio de mensagem em massa

## Bibliotecas
import pyautogui
import webbrowser
from time import sleep

## Código

# Lista dos contatos
# contatos = [5594992238197, 5594981197102]

# # Laço de repetição
# for telefone in contatos:
#     webbrowser.open(f'http://api.whatsapp.com/send?phone={telefone}')
#     sleep(20)
#     pyautogui.typewrite('Teste de automação, envio de mensagens em massa, via WhatsApp')
#     sleep(5)
#     pyautogui.press('enter')
#     sleep(60)

## Lista de um arquivo .txt
contatos = []

with open('Contatos.txt','r') as arquivos:
    for linhas in arquivos:
        contatos.append(linhas.split('\n')[0])
    print(contatos)

# Laço de repetição
for telefone in contatos:
    webbrowser.open(f'http://api.whatsapp.com/send?phone={telefone}')
    sleep(20)
    pyautogui.typewrite('Teste de automação, envio de mensagens em massa, via WhatsApp')
    sleep(5)
    pyautogui.press('enter')
    sleep(60)
