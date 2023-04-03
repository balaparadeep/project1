import pyautogui
import time
import pyttsx3

user_text = input('Enter a text :')
print('please wait few seconds...it will be done')

def speak(hlo):
    time.sleep(1)
    sound = pyttsx3.init()
    rate = sound.getProperty('rate')
    sound.setProperty('rate', 120)
    voices = sound.getProperty('voices')
    sound.setProperty('voice', voices[1].id)
    print('speaking......')
    sound.say(hlo)
    sound.runAndWait()
    print('completed')


def bombit(it):
    pyautogui.write(it)
    pyautogui.press('Enter')
    print('delivered','.'*20)


msg = int(input('Enter how many messages you want :'))
time.sleep(5)
if msg != 0:
    for i in range(msg):
        print('if you want to exit bombit press 0...')
        print('sending messages ..............')
        bombit(user_text)
else:
    print('its ok try later')
    speak(user_text)

print('Thank you❤️❤️👍👍')



