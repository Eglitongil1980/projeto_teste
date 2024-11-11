# Usando a função click
import pyautogui
from time import sleep
import pyperclip # Usar caracteres especiais

# Click personalizado
# pyautogui.click(x=856,y=543, clicks=21, interval=0.1, button='left', duration=2)

# # Click na posição atual
# pyautogui.click()
# pyautogui.click('left')
# pyautogui.click('right')
# pyautogui.click('middle')

# # Funções prontas
# pyautogui.doubleClick()
# pyautogui.rightClick()
# pyautogui.tripleClick()
# pyautogui.middleClick()

#Mover o mouse e abir uma pasta

# pyautogui.rightClick(x=913,y=551, duration=2)
# pyautogui.move(200,0, duration=2)
# pyautogui.click()

# Arrastando e soltando as coisas

# for i in range(1):
#     # Mover até uma coordenada
#     pyautogui.moveTo(x=475,y=429, duration=2)
#     # Clicke a arrastar até o ponto final
#     pyautogui.dragTo(x=1634,y=321, duration=2)

# Como usar a rolagem do mouse
# pyautogui.moveTo(x=1270,y=496, duration=2)
# for i in range(5):
#     pyautogui.scroll(-2500)
#     sleep(2)

# Como digitar em qualquer lugar

# def escrever_frase(frase):
#     pyperclip.copy(frase)
#     pyautogui.hotkey('ctrl','v')

# pyautogui.moveTo(x=1128,y=994, duration=2)
# pyautogui.click()
# #pyautogui.typewrite('Olá, primeiro teste de automação no whatsapp')
# escrever_frase('Olá, primeiro teste de automação no whatsapp')
# pyautogui.click(x=1889,y=985,duration=2)

#Como automatizar sistemas usando teclado

# Navegar até o campo do e-mail
# pyautogui.click(x=1544,y=542, duration=2)
# # Digite o email
# pyautogui.typewrite('egliton@hotmail.com')
# # Apertar o Tab
# pyautogui.press('tab')
# # Digite a senha
# pyautogui.typewrite(12345)
# # Apertar o Tab
# pyautogui.press('tab')
# # Apertar Space
# pyautogui.press('space')

# Para ve todas as possiveis teclas
# print(pyautogui.KEYBOARD_KEYS)

# Como usar os botões e teclas de atalhos
# pyautogui.click(x=1333,y=251,duration=2)
# pyautogui.hotkey('ctrl','a')
# pyautogui.hotkey('ctrl','c')
# pyautogui.click(x=1639,y=691,duration=2)
# pyautogui.hotkey('ctrl','v')

# Tirando prints da tela

# Print da tela inteira
# pyautogui.screenshot('tela.png')
# Print da personalizado
pyautogui.screenshot('passagem.png', region=(500,596,1000,300))
