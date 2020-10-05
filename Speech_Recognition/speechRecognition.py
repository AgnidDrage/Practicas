import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something...")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("What did you said: {}".format(text))
    except:
        print("I didn't understand you")