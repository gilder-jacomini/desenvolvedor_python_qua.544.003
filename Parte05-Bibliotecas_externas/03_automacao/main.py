import pyautogui as auto



def ir_pesquisa():
    auto.press('tab')
    auto.press('tab')
    auto.press('tab')
    auto.press('tab')

def main():
    auto.PAUSE = 1
    auto.press('win')
    auto.write('firefox')
    auto.press('enter')
    auto.write('youtube.com')
    auto.press('enter')
    auto.sleep(5)
    ir_pesquisa()
    auto.write('python')
    auto.press('enter')
    auto.sleep(5)
    auto.hotkey('ctrl', 't')
    auto.write('https://python.org')
    auto.press('enter')



if __name__ == "__main__":
    main()