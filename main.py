#from body.listen import listen
from body.speak import Speak
from features.clap import Tester

def main():
    Tester()
    Speak("Hello sir!")

if __name__ == "__main__":
    main()
    