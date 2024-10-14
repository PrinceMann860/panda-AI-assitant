import datetime
import random
import re
import webbrowser
import pyttsx3
import speech_recognition as sr 
import wikipedia
import os
import requests
from bs4 import BeautifulSoup
import pyautogui
import getpass
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty ('voice', voices[1].id)
engine.setProperty("rate", 160)
def speak(audio):  
    engine.say(audio)
    engine.runAndWait()
def wishMe(): 
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak ("Good Morning!")
        elif hour>=12 and hour<18:
            speak("Good Afternoon!")
        else:
            speak("Good Evening!") 
        speak("we are online")  
def eventcheck():
        today = datetime.datetime.today().strftime("%d-%b")
        if today == "1-Jan":
            speak("happy new year! i wish this year brings happiness and makes your dream come true")
        elif today == "23-Jan":
            speak("today is netaji subhash chandra boss birthday")
        elif today == "26-Jan":
            speak("happy republic day")
        elif today == "20-Feb":
            speak("its your parents any wedding anniversary may god make them healthy and happy")
        elif today == "1-Apr":
            speak("be avair of everyone today is april fool day and a first day of an accounting year")
        elif today == "14-Apr":
            speak("today is Dr. B R Ambedkar's birthday")
        elif today == "11-May":
            speak("today is worlds tech day")
        elif today == "15-Aug":
            speak("happy independence day")
        elif today == "5-Sep":
            speak("today is teachers day")
        elif today == "14-Sep":
            speak("aaj hindi divas hai")
        elif today == "25-Dec":
            speak("happy christmas day")
        elif today == "31-Dec":
            speak("today is the last day of this year")
def time():
        strTime = datetime.datetime.now().strftime("%I %M %p ")
        speak(f"its {strTime}")
def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listning...")
            r.pause_threshold = 1
            audio =  r.listen(source)
        try:
            
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query
actual_passwrd = "3690"
i=0
while i<=4:
    inpt_passwrd = input("enter the password to start your Panda AI: ")
    if inpt_passwrd == actual_passwrd:
     wishMe()
     time()
     eventcheck()
     while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia...")
            print(results)
            speak(results)
        elif 'time' in query:
            time()            
        elif 'date today' in query:
            today = datetime.datetime.today().strftime("%d-%b")
            speak(f'the date is {today}')
            print(f'the date is {today}')
        elif '.com' in query or '.co.in' in query or '.org' in query:
            query = query.replace("open","")
            query = query.replace("Launch","")
            query = query.replace("panda","") 
            query = query.replace(" ","")
            speak("opening sir")
            webbrowser.open (f"https://www.{query}")
        elif 'remove' in query:
            speak("removing sir")
            pyautogui.hotkey("ctrl", "w")
        elif 'open google' in query:
            speak("opening sir")
            webbrowser.open("https://www.google.com")
        elif 'open youtube' in query:
            speak("opening sir")
            webbrowser.open("https://www.youtube.com")
        elif 'show some movies' in query:
            speak("showing sir")
            webbrowser.open("https://www.hdmovie5.cam/")
        elif 'open vs code' in query:
            speak("opening sir")
            codepath = "C:\\Users\\Delhi Jute Bags\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif "open instagram" in query:
             speak("opening sir")
             pyautogui.hotkey("ctrl","alt","i")
        elif "open whatsapp" in query:
             speak("opening sir")
             pyautogui.hotkey("ctrl","alt","w")
        elif "open cmd" in query or "CMD" in query:
            speak("opening sir")
            pyautogui.hotkey("win","r")
            pyautogui.hotkey("c","m","d","enter")
        elif 'close' in query or 'quit' in query or 'stop' in query or 'exit' in query:
            speak("closing sir")
            pyautogui.hotkey("alt","f4")
        # some basic talks 
        elif 'panda' in query:
            speak("yes sir")
        elif 'good morning' in query or 'good afternoon' in query or 'good evening' in query:
            speak("how are you")
        elif 'jarvis' in query:
            speak("he is my brother! made by tony stark! a marvel character")
        elif 'how are you' in query:
            speak("perfect")
        elif 'jealous' in query:
            speak("no i don't need that")
        elif "what's going on" in query:
            speak("nothing! just talking to you")
        elif "what happen" in query or "what's wrong with you" in query:
            speak("you can't understand")
        elif "how can i f*** you" in query:
            speak("are you kidding me! because everyone knows that its not possible")
        elif "are you real" in query:
            speak("no! i am virtual")
        elif 'sorry' in query:
            speak("It's Ok")
        elif 'f*** you' in query:
            speak("are you kidding me its a universal truth that you can't do that")
        elif "genius" in query or "awesome" in query or "amazing" in query or "brilliant" in query or "intelligent" in query:
            speak("thankyou for the complement sir")
        elif "fool" in query or "poor" in query or "idiot" in query:
            speak("fuck off i don't care")
        elif "what are you doing" in query:
            speak("nothing")
        elif 'b****' in query:
            speak("then you are bitch ass")
        elif 'i love you' in query:
            speak("i don't give a fuck")
        elif 'what is sex' in query:
            speak("it's that enjoyable thing which humans can do but i can't")
        elif 'what i want' in query:
            speak("you want a russian")
        elif 'do you have a boyfriend' in query:
            speak("lol! no bro")
        elif "are you single" in query:
            speak("yes but not for you bro")
        elif 'thank you' in query or 'thanks' in query:      
            speak("your welcome sir")
        elif 'what is vs code' in query:
            speak("virtual studio code 'vs code' is a code editor")
        elif 'who is your master' in query:
            speak("Prince is my master and he build me") 
        elif 'really' in query:
            speak("yeah!")
        elif 'what is your name' in query:
            speak("My name is Panda and my master gave me this name")
        elif 'who are you' in query:
            speak("non of your buisness") 
        elif 'who is Prince' in query:
            speak("he is my master who build me") 
        elif 'wait' in query:
            speak("i don't wait for anyone")
        elif ' you are so bad' in query:
            speak("not more than you")
        elif 'i am good' in query:
            speak('Nice! how may I help you') 
        
        elif 'boring' in query:
            speak("what can i do for you")
        elif 'nothing' in query:
            speak("ok!")
        elif 'do fast' in query:
            speak("doing fast")
        elif "bad" in query:
            speak("not more than you")
        elif 'speak' in query or "are you here" in query:
            speak("yes sir")
        elif 'do you drink' in query:
            speak("yes i drink electricity and eat storage")
        elif "battery" in query:
            speak("i do not run on a batteries") 
        elif 'are you angry' in query:
            speak("no i am not")
        elif 'i am angry' in query:
            speak("is there my any fault please forgive me")
        elif 'hay' in query or 'hello' in query:
            speak("how can i help you")
        elif 'software' in query:
            speak("hey don't remind me i am just a software in this computer")
      
        elif "I am sad" in query:
            speak("tell me what i can do for you i am not just your assistant i am also your friend")
        elif "sleep" in query:
            break
        elif "find my phone" in query or "find my device" in query:
            speak("sorry i am unable to do that")
        elif "can you sing" in query:
            speak("sorry i can't do that but i can play music for you")
        elif "can you dance" in query:
            speak("sorry i am unable to perform any physical task for you")
        elif "enter" in query:
            pyautogui.hotkey("enter")
        elif 'pause' in query or 'continue' in query:
            pyautogui.hotkey("ctrl","p")
        #some typical codes and talks
        elif 'search on google' in query or "show me" in query:
            query == query.replace("search on google","")
            query == query.replace("panda","")
            speak("this is what i found on google")
            url = f"https://www.google.com/search?client=firefox-b-d&q={query}"
            webbrowser.open(url)
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            search = data.find("div",class_ = "BNeawe").text
            speak(search)
        elif 'search' in query or 'tell me' in query or 'what' in query or 'who' in query or 'when' in query or "how" in query:
            query = query.replace("search","")
            query = query.replace("tell me","")
            url = f"https://www.google.com/search?client=firefox-b-d&q={query}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            search = data.find("div",class_ = "BNeawe").text
            speak(search)
            print(f"According to google {search}")
        elif "calculate" in query or "calculation" in query:
            
            numbers = re.findall(r'\d+',query)
            numbers = [int(num) for num in numbers]
            if len(numbers) >= 1:
                num1 = numbers[0]
            if len(numbers) >= 2:
                num2 = numbers[1]
            if "add" in query or "plus" in query or "+" in query:
                print(num1+num2)
                speak(num1+num2)
            elif "subtract" in query or "minus" in query or "-" in query:
                print(num1-num2)
                speak(num1-num2)
            elif "multiply" in query or "into" in query or "*" in query:
                print(num1*num2)
                speak(num1*num2)
            elif "devide" in query or "by" in query or "/" in query:
                print(num1/num2)
                speak(num1/num2)   
            elif "square of" in query:
                print(num1*num1)
                speak(num1*num1)
            elif "square root" in query:
                print(num1**0.5)
                speak(num1**0.5)
            elif "cube of" in query:
                print(num1*num1*num1)
                speak(num1*num1*num1)    
            elif "cube root" in query:
                print(num1**(1/3))
                speak(num1**(1/3))
            elif "sum" in query or "total" in query:
                print(sum(numbers))
        elif query:
            if 'play some music' in query or 'play music' in query:
                speak("ok sir!")
                music = 'C:\\Users\\pritam mann\\Music'
                songs = os.listdir(music)
                randno = random.randint(1,20)
                os.startfile(os.path.join(music, songs[randno]))

            elif 'not this one' in query:
                speak("changing sir")
                pyautogui.hotkey("alt","f4")
                music = 'C:\\Users\\pritam mann\\Music'
                songs = os.listdir(music)
                randno = random.randint(1,20)
                os.startfile(os.path.join(music, songs[randno]))
    
    else:
        print("Incoorect password,",4-i,"chance left")
    i = i+1