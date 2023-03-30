import pyttsx3

talk = pyttsx3.init()
rate = talk.getProperty('rate')
talk.setProperty('rate', 120)
print('speaking.....')
text_speech = 'hi welcome to python programming'
talk.say(text_speech)
talk.runAndWait()
text_speech =  'you can chat with me'
talk.say(text_speech)
talk.runAndWait()
print('    ****************',text_speech,'*****************')
print('***************** converting text into speech *****************')
print('    ****************',text_speech,'****************')
while text_speech != 'bye':
    text_speech = input("Text here I speak outside : ")
    text_speech = text_speech.lower()
    talk.say(text_speech)
    talk.runAndWait()

    print('reply                     :',text_speech)
print('\nConversation is ended..')
print('Completed....Done.')



