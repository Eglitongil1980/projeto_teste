# Usando a função click
import pyautogui

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

for i in range(1):
    # Mover até uma coordenada
    pyautogui.moveTo(x=475,y=429, duration=2)
    # Clicke a arrastar até o ponto final
    pyautogui.dragTo(x=1634,y=321, duration=2)