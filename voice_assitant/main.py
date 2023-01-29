import pyttsx3

speech = pyttsx3.init()
speech.setProperty("rate", 150)

def female() :
    voices = speech.getProperty("voices")   
    speech.setProperty("voice", voices[1].id)

gender = input("WHICH GENDER ARE YOU ?")

if(gender == "female") :
    female()

print("GENDER FIXED")

text = ""

while(text != "stop" ) :
    text = input("ENTER YOUR THOUGHTS :")
    print(text)
    if(text == "stop") :
        continue
    speech.say(text)
    speech.runAndWait()
    