# Api key
fileopen=open("","r" )
API=fileopen.read()
fileopen.close()

print(API)
import openai 
from dotenv import load_dotenv
 
 #coding

openai.api_key=API
load_dotenv()
completion=openai.completion()

def ReplyBrain(question,chat_log=none):
 filelog=openai("","r")
 chat_log_template=Filelog.read()
 Filelog.close()

 if chat_log is None:
  chat_log=chat_log_template

  prompt=f{chat_log}You : {question}\njarvis :}
  response=completion.create(
   model="text-davinci-002",
   prompt=prompt,
   temperature=0.5,
   max_tokens=60,
   top_p=0.3,
   frequency_penalty=0.5,
   presense_penalty=0)
  answer=response.choices[0].text.strip()
  chat_log_template_update=chat_log_template+f"\nYou : {question} \njarvis : {answer}"
  filelog=open("","w")
  filelog.write(chat_log_template_update)
  filelog.close()
  return answer
 
 ReplyBrain("hello,how are you?")

while True:
 kk= input("enter : ") 
 print(ReplyBrain(kk))