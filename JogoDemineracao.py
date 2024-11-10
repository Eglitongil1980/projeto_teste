# Jogo de Mineração
# https://www.crazygames.com/game/doge-miner-2?_gl=1*r0dm1o*_ga*MjA0MjUyMDA1NS4xNzI5NDI2ODQ3*_ga_37GXT4VGQK*MTczMTI2Mjg1MC4xOC4xLjE3MzEyNjMyNTUuMC4wLjA.

import pyautogui
from time import sleep

pyautogui.moveTo(x=1329,y=523,duration=2)
for i in range(500):
    sleep(0.1)
    pyautogui.click()