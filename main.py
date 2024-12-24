import os
import sys
from time import sleep

import clipboard
import keyboard
import pyautogui as py


def countdown(seconds):
    for i in range(seconds, -1, -1):
        sys.stdout.write(f"\rWait {i} Secs")
        sys.stdout.flush()
        sleep(1)


def open_whatsapp_exe():
    os.system('start whatsapp://send?phone=XXXXXXXXXXX')

    count = 0

    while count < 5:
        countdown(1)
        count += 1

        # Validate that the program opened correctly
        try:
            py.locateCenterOnScreen('assets\\Number.png', confidence=.9, grayscale=True)
            return True
        except py.ImageNotFoundException as imError:
            print(imError)
            py.alert('Check WhatsApp, contact not found!\nClosing[...]')
            return False


def send_message():
    if open_whatsapp_exe():
        # x, y = py.locateCenterOnScreen('assets\\Number.png', confidence=.9, grayscale=True)
        # py.click(x, y)
        for phrase in get_phrases():
            if keyboard.is_pressed('esc'):
                response = py.confirm(text='The program will be closed, do you want to continue?', title="WHAT's Bot",
                                      buttons=['OK', 'Cancel'])
                if response == 'OK':
                    sys.exit()
                else:
                    countdown(2)
                    continue
            else:
                clipboard.copy(phrase)
                py.hotkey('ctrl', 'v')
                py.press('enter')


def get_phrases():
    with open('assets\\Frases.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        phrases = [line.strip() for line in lines]
        return phrases


if __name__ == '__main__':
    open_whatsapp_exe()
