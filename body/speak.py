# speak function - two speak functions
# 1) windows based - pip install pyttsx3
# 2) chrome based - pip install selenium==4.1.3

# 1) windows based:
# advantages are, it is fast and it can work in offline.
# disadvantages are, we can't overspeak and it has less voice's options. 

#import pyttsx3

#def Speak(Text):
   # engine = pyttsx3.init("sapi5")
   # voices = engine.getProperty('voices')
   # engine.setProperty('voices',voices[0].id)
   # engine.setProperty('rate',170)
   # print("")
   # print(f"You : {Text}.")
   # print("")
   # engine.say(Text)
   # engine.runAndWait()

# 2) chrome based:
# advantages are, it has more voices options,it is more clear,it will allow overspeaking.
# disadvantages are, it has word limit and it will work slow.

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True
Path = "database\chromedriver.exe"
driver = webdriver.Chrome(Path,options=chrome_options)
driver.maximize_window()

website = r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
buttonselection = Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
buttonselection.select_by_visible_text('British English / Brian')

def Speak(audio):

    lengthoftext = len(str(audio))

    if lengthoftext==0:
        pass
    else:
        print("")
        print(f"JARVIS : {audio}")
        print("")
        Data = str(audio)
        xpathofsec = '/html/body/div[4]/div[2]/form/textarea'
        driver.find_element(By.XPATH,value=xpathofsec).send_keys(Data)
        driver.find_element(By.XPATH,value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH,value="/html/body/div[4]/div[2]/form/textarea").clear()
        
        if lengthoftext>=30:
            sleep(4)

        elif lengthoftext>=40:
            sleep(6)

        elif lengthoftext>=50:
            sleep(8)

        elif lengthoftext>=70:
            sleep(10)

        elif lengthoftext>=100:
            sleep(12)

        elif lengthoftext>=120:
            sleep(14)  
        else:
            sleep(2)

