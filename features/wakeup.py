import speech_recognition as sr 
import os

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")

    except:
        return ""

    query = str(query.lower())
    print(query)
    return query

def WakeupDetected():
    query = listen().lower()

    if "wake up" in query:
        os.startfile(r"C:\Users\Vijay\PycharmProjects\advance jarvis\main.py")
    else:
        pass    

while True:
    WakeupDetected()
