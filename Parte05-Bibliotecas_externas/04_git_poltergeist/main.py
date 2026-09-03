import pyautogui as auto
from datetime import date

def hoje():
    return date.today().strftime("%d/%m/%Y")

def main():
    auto.PAUSE = 0.75
    auto.press('win')
    auto.write('vs code')    
    auto.press('enter')
    auto.sleep(10)
    auto.hotkey('ctrl', 'j')
    auto.sleep(10)
    auto.write('cd C:\Users\ALUNO\Gilder\desenvolvedor_python_qua.544.003')
    auto.press('enter')
    auto.write('git add .')
    auto.press('enter')
    auto.write(f'git commit -m "Aula dia {hoje()}"')
    auto.press('enter')
    auto.write('git push')
    auto.press('enter')
               
if __name__ == "__main__":
    main()