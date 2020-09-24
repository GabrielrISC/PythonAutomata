import pyautogui as comando
import time
from reader.__main__ import main

if __name__ == '__main__':
    
    comando.hotkey('winleft', 'r',interval =0.1)
    comando.typewrite('chrome --incognito',interval =0.1)
    comando.press('enter',interval =0.1)

    time.sleep(3)

    #Maximizar pantalla
    comando.moveTo(580, 45)
    comando.click()

    comando.typewrite('ngmesasv.auto.contiwan.com:8861/iGate/pulse')
    comando.press('enter')

    time.sleep(3)

    var = comando.locateCenterOnScreen('reporting.PNG')
    comando.moveTo(var)
    time.sleep(2)
    var = comando.locateCenterOnScreen('analitics.PNG')
    comando.moveTo(var)
    comando.click()
