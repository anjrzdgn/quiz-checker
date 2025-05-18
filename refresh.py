import webbrowser
import pyautogui
import time
import pyperclip
import pygame
import os

url = "https://yekta.iut.ac.ir/course/view.php?id=49081"
last_clipboard = ""
max_size = 0
flag_second_bigger = 0
times = 0
while True:
    pyautogui.hotkey('ctrl', 'w')   #close
    pyautogui.hotkey('ctrl', 'w')   #close
    webbrowser.open(url)
    time.sleep(1.5)

    pyautogui.hotkey('ctrl', 'u')   #page html
    time.sleep(1.5)

    pyautogui.hotkey('ctrl', 'a')   #select
    time.sleep(0.2)

    pyautogui.hotkey('ctrl', 'c')   #copy
    time.sleep(0.3)

    current_clipboard = pyperclip.paste()

    if current_clipboard:
        size_in_bytes = len(current_clipboard.encode('utf-8'))
        if size_in_bytes > max_size:
            max_size = size_in_bytes

            if flag_second_bigger:
                pygame.mixer.init()
                sound = pygame.mixer.Sound("sound.wav")
                os.startfile("pic.png")
                sound.play()
                time.sleep(7)
                exit()

        times += 1
        print(times, f"Exact size of the HTML message: {size_in_bytes} bytes\n")
        flag_second_bigger = 1
        last_clipboard = current_clipboard

    time.sleep(15)
