# Bibliotecas
import webbrowser
import pyautogui	
import pyperclip
from time  import sleep

# def escrever_frase(frase):
#     pyperclip.copy(frase)
#     pyautogui.hotkey('ctrl','v')

# 	# 1. Abrir o navegador no site Instagram
# webbrowser.open('https://www.instagram.com/')
# sleep(10)
# 	# 2. Navegar até Pesquisa
# pyautogui.click(x=123,y=361, duration=2)
# 	# 3. Clicar em Pesquisa
# pyautogui.click(x=220,y=282, duration=2)
# 	# 4. Ir até o campo pesquisar e colar
# escrever_frase('Caiçara')
# sleep(3)
# 	# 7. Descer e clicar na página
# pyautogui.click(x=252,y=334, duration=2)
# sleep(3)
# 	# 8. Rolar um pouco para baixo
# pyautogui.click(x=701,y=915, duration=2)
# 	# 9. Verificar se foi curtido
# CurtidaCoracao = pyautogui.locateCenterOnScreen('CurtidaCoracao.png')
# sleep(1)
# 	# 10. Se já tiver curtido, não fazer nada e pause por 60 segundos
# if CurtidaCoracao is not None:
# 	sleep(60)
# elif CurtidaCoracao == None:
#       pyautogui.click(x=1089,y=819,duration=2)
	# 11. Comentar
	# 12. Clicar em comentar
	# 13. Clicar em fechar a janela
	# 14. Fechar o navegador
	# 15. Pausar por 24 horas
	# 16. Após as 24 horas voltar a rodar
      
webbrowser.open('https://cpstest.org/100-seconds.php?_gl=1*1pu3mlv*_ga*MjA0MjUyMDA1NS4xNzI5NDI2ODQ3*_ga_37GXT4VGQK*MTczMTI2Mjg1MC4xOC4xLjE3MzEyNjQ3MTcuMC4wLjA.')
teste = pyautogui.locateCenterOnScreen('teste.png')
pyautogui.click(x=592,y=826,duration=2)
