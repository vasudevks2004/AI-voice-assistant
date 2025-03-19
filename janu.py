import speech_recognition as me
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
from ecapture import ecapture as ec
import cv2 

listener = me.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ""
    try:
        with me.Microphone() as sorce:
            print("listening....")
            voice= listener.listen(sorce)
            command= listener.recognize_google(voice)
            command= command.lower()
            if "janu" in command:
                command= command.replace("janu","")
                print(command)
            else:
                print("wrong command")
            
    except Exception as e:
        print(e)
        pass        
    return command

def evaluate_math_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        print(e)
        return "Sorry, I couldn't understand the mathematical expression."
def run_janu():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play","")
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time= datetime.datetime.now().strftime("%I:%M %p")
        talk("current time is" + time)
    elif "who is" in command:
        person= command.replace("who is","")
        info= wikipedia.summary(person,2)
        print(info)
        talk(info)
    elif "date" in command:
        talk("sorry i have losemotion")
    elif "tell me a joke" in command:
        joke=pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif " who found you" in command:
        talk("my founders name is vasudev")
    elif "are you single" in command:
        talk("sorry i am in love with my founder vasudev")
    elif "how are you" in command:
        talk("i am fine thank you")
    elif "bie" in command:
        talk("jannu is siningof")
    elif "search" in command:
        command = command.replace("search","")
        webbrowser.open_new_tab(command)
        time.sleep(5)
    elif "kiss" in command:
        talk("muahhh")
    elif "camera" in command or "take a photo" in command:
        ec.capture(0,"robo camera","img.jpg")
    elif "video" in command or "take a video" in command:
        cv2.videocapture(0)
    elif "calculate" in command or "what is" in command:
        expression = command.replace("calculate", "").replace("what is", "")
        result = evaluate_math_expression(expression)
        talk(result)
        print(result)
    else:
        print ("sorry i didnt catch that")

while True:
    run_janu()
