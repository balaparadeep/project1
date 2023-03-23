import pyttsx3
import time
import pywhatkit
import pyautogui


py = pyttsx3.init()
txt = input("Enter a text :")





def func():
    rate = py.getProperty('rate')
    py.setProperty('rate', 100)
    voices = py.getProperty('voices')
    py.setProperty('voice',voices[1].id)
    print('speaking...')
    py.say(txt)
    py.runAndWait()

while txt not in ('bye','BYE','Bye','BYe'):

    txt = input("what should i enter :")
    func(txt)


