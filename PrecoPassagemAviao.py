import pyautogui
from time import sleep

# Clicar na aba
pyautogui.click(x=1532,y=15, duration=2)
sleep(2)
# Clicar para atualizar a página
pyautogui.click(x=88,y=68, duration=2)
sleep(10)
# Print da personalizado
pyautogui.screenshot('passagem.png', region=(500,596,1000,300))
sleep(5)
pyautogui.click(x=1118,y=1042,duration=2)
pyautogui.click(x=447,y=300,duration=2)
# pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('ctrl','c')
pyautogui.click(x=1228,y=1050,duration=2)
pyautogui.click(x=743,y=989,duration=2)
pyautogui.hotkey('ctrl','v')
pyautogui.click(x=1219,y=960,duration=2)
# pyautogui.click(x=1888,y=988,duration=2)