from brain.AIBrain import ReplyBrain 
from body.listen import MicExecution
from brain.qna import QuestionAnswer
print(">> starting The jarvis : Wait for some seconds.")
from body.speak import speak
from features.clap import Tester
print(">> starting the jarvis : wait for few seconds more")

def mainexecution():

    speak("hello sir")
    speak("i am jarvis,i am ready to assist you")
   
    while True:

        data = MicExecution()
        data = str(data)

        if int(data)<3:
            pass
        
        elif "turn on the tv" in data:
            speak ("ok ..turning on the android tv")
            
        elif "what is" in data or "where is" in data or "question" in data or "answer" in data:
            reply=QuestionAnswer(data)

        else:
            reply=ReplyBrain(data)
            speak(reply)
            

        

def clapDetect():

    query=Tester()
    if "true-mic" in query:
        print("")
        print(">> clap detected!! >>")
        print("")
        mainexecution() 
    else:
        pass

    clapDetect()