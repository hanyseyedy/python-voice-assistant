import speech_recognition as sr

END_PHRASE = 'پایان'


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            return r.recognize_google(audio, language='fa-IR')
        except:
            return 'متوجه نشدم! 🤔'


while True:
    print(f'اگه میخوای خارج بشی لطفا بگو "{END_PHRASE}"')
    print(' دارم بهت گوش میدم... 🦻')
    text = get_audio()
    print('\033[1m' + text + '\033[0m')
    if text.find(END_PHRASE) == 0:
        print('🤚🤚🤚 خداحافظ')
        break