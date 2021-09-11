import pywhatkit as pt
import speech_recognition as sr
import requests
import smtplib
import pyttsx3
import datetime
import os
import sys
import pyjokes
import webbrowser
import cv2
import wikipedia
import random
from time import strftime
import python_weather
import asyncio
import pyautogui
import PyPDF2
import calendar
from faker import Faker

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

Paasword =  True
while Paasword:
    speak(" If you want to acess the program enter the paasword User..")
    Paasword = int(input("Enter The paasword User.."))

    if Paasword != 24:
         speak("Acess denied")
         print("Acess denied")

    if Paasword == 24:
        Paasword = False
        speak("Acess Granted")
        print("Acess Granted")

        speak("Identity recognised")
        print("Identity recognised")

def wishMe():
   hour = int(datetime.datetime.now().hour)
   if hour>=0 and hour<12:
       speak("Good Morning!")

   elif hour>=12 and hour<18:
       speak("Good Afternoon!")

   else:
       speak("Good Evening!")

   speak("I am Cooper Sir . Please tell me how may I help you")
   
def takeCommand():
    #It takes Micrrophone input

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rudrejalsingh@gmail.com', 'SARITAWB1123')
    server.sendmail('rudrejalsingh@gmail.com', to, content)
    server.close()

def pdf_reader():
    book = open('The Hobbit.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total pages in book {pages}")
    print(f"Total pages in book {pages}")
    speak("Sir which page you wanna read")
    print("Sir which page you wanna read")
    pg = int(input("Enter the page no. "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)
    

def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=fc84cc7845ae4ac992b56d6f527d87f8'

    main_page = requests.get(main_url).json()
    #print(main_page)
    articles = main_page["articles"]
    #print(articles)
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")
        

if __name__ == "__main__":
    wishMe()
    while True: # I can turn it on
        
        query = takeCommand().lower()

        # Uses logic to execute command
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")#It is actually 2
            results = wikipedia.summary(query, sentences=3)#I  determine the amount of information I shall need
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'calendar' in query:
            year =int( input("Enter the year of the required calendar "))
            month = int( input("Enter the month of the required calendar "))
            print(calendar.month(year,month))

        elif 'who am i' in query:
            fake = Faker()
            print(fake.name())
            print(fake.email())
            print(fake.country())
            
        elif 'open command prompt' in query:
            print("Here you go sir")
            speak("Here you go sir")
            os.system("start cmd")

        elif 'open camera' in query:
           print("Opening camera sir..")
           speak("Opening camera sir..")
           cap = cv2.VideoCapture(0)
           while True:
               ret, img = cap.read()
               cv2.imshow('webcam', img)
               k = cv2.waitKey(50)
               if k ==27:
                    break;
           cap.release()
           cv2.destroyAllWindows()

        elif 'play music' in query:
            music_dir = "D:\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif 'joke' in query:
            while True:
                jokes = pyjokes.get_joke(language="en", category="neutral")
                print(jokes)
                speak(jokes)
                speak("Do you want to hear a joke again")
                jk = input("Do you want to hear a joke again ? (y/n)")
                if jk.lower() == 'n':
                    break

        elif 'news' in query:
            print("Sir fetching the latest news")
            speak("Sir fetching the latest news")
            news()

        elif 'weather' in query:
            print("Of which place sir?")
            speak("Of which place sir?")
            mm = takeCommand().lower()
            async def getweather():
                # declare the client. format defaults to metric system (celcius, km/h, etc.)
                client = python_weather.Client(format=python_weather.IMPERIAL)

                # fetch a weather forecast from a city
                weather = await client.find(f"{mm}")

                # returns the current day's forecast temperature (int)
                print(weather.current.temperature)
                speak(weather.current.temperature)
    
                # get the weather forecast for a few days
                for forecast in weather.forecasts:
                    print(str(forecast.date), forecast.sky_text, forecast.temperature)
                    speak(str(forecast.date))
                    speak(str(forecast.sky_text))
                    speak(str(forecast.temperature))

                # close the wrapper once done
                await client.close()

            if __name__ == "__main__":
                loop = asyncio.get_event_loop()
                loop.run_until_complete(getweather())

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")

        elif 'open code' in query:
            codePath = "E:\\coding\\visual studio code\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to rudra' in query:
            try:
                speak("What should I say?")
                print("What should I say?")
                content = takeCommand().lower()
                to = "udrejalsingh@gmail.com"
                sendEmail(to, content)
                speak("Your Email has been sent to rudra")
                print("Your Email has been sent to rudra")

            except Exception as e:
                print(e)
                speak("Sorry sir , Due to some reason I am not able to send this email")

        elif 'open youtube' in query:
            print("Opening youtube sir")
            speak("Opening youtube sir")
            pt.search("www.youtube.com")

        elif 'open google' in query:
            print("opening google sir..")
            speak("opening google sir..")
            print("Sir what should I search on google")
            speak("Sir what should I search on google")
            cm = takeCommand().lower()
            pt.search(f"{cm}")

        elif 'send message' in query:
            pt.sendwhatmsg("+919432591091", "Hi Papa",17,7)

        elif 'book' in query:
            pdf_reader()

        elif 'play youtube' in query:
            print("Right away sir")
            speak("Right away sir")
            print("What should I search sir")
            speak("What should I search sir")
            sr = takeCommand().lower()
            pt.playonyt(f"{sr}")
            break

        elif 'open stackoverflow' in query:
            print("opening the flow sir..")
            speak("opening the flow sir..")
            pt.search("www.stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")

        elif 'dino swords' in query:
            print("opening dino swords sir..")
            speak("opening dino swords sir..")
            pt.search("dinoswords.com")

        elif 'battle dudes io' in query:
            print("opening the dungeon sir..")
            speak("opening the dungeon sir..")
            webbrowser.open("aidungeon.com")

        elif 'open epicgames' in query:
            print("opening  sir..")
            speak("opening  sir..")
            pt.search("epicgamesstore.com")

        elif 'open steam' in query:
            print("opening steam  sir..")
            speak("opening steam  sir..")
            pt.search("steam.com")

        elif 'bored button' in query:
            print("opening bored button  sir..")
            speak("opening bored button  sir..")
            pt.search("boredbutton.com")

        elif 'you are the best' in query:
            print("Thank you sir for the compliment")
            speak("Thank you sir for the compliment")

        elif 'who are you?' in query:
            print("I am your personal AI - Cooper")
            speak("I am your personal AI - Cooper")

        elif 'change your voice ' in query:
            print("Please go to the user setting")
            speak("Please go to the user setting")

        elif 'bye' in query:
            print("Thank you for having me here sir....")
            speak("Thank you for having me here sir....")
            sys.exit()

        elif 'thank you' in query:
            print("You are welcome sir")
            speak("You are welcome sir")

        elif 'what is your name' in query:
            print("I am cooper your personal assistant sir..")
            speak("I am cooper your personal assistant sir..")

        elif 'fire up' in query:
            print("BOOM I am here sir")
            speak("BOOM I am here sir")

        elif 'play dice' in query:
            print("Right away sir!!!")
            speak("Right away sir!!!")

            def rolldice(min,max):
                while True:
                    print("Rolling dice sir...")
                    speak("Rolling dice sir...")
                    number = random.randint(min,max)
                    print(f" Sir your number is : {number}")
                    speak(f"Sir your number is : {number}")
                    print("Do you wanna play again?")
                    speak("Do you wanna play again?")
                    choice = takeCommand().lower()
                    if choice.lower() == 'no':
                        print("Thank you sir")
                        speak("Thank you sir")
                        break
                    
            rolldice(1, 6)
