import pyautogui
import time
# NOTE : You must be logged in whatsapp web in your device browser then only it works
msg = input('Enter a message :')
limit = int(input('Enter a limit in numbers :'))
count = 1
print('Sending....')
time.sleep(5)

def bombit(name):
    pyautogui.write(name)
    pyautogui.press('Enter')

while count < limit:
    bombit(msg.upper())
    count += 1
print('Successfully delivered...')



