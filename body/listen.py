#telugu-hindi-english:command
#understands in english

#step-1: pip install googletrans

#step-2: creating three functions
# 1) listening function
# 2) translating to english function
# 3) connecting

import speech_recognition as sr
from googletrans import Translator

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"You said: {query}")
            return query
        except Exception as e:
            print(f"Sorry, an error occurred: {e}")

listen()


# 2) translating to english function

def TranslationHinToEng(audio):
    line = str(audio)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"you : {data}.")
    return data

# 3) connecting

def MicExecution():
    query = listen()
    data = TranslationHinToEng(query)
    return data

