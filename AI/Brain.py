import subprocess
import wolframalpha
#from ecapture import ecapture as ec
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')

rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
voice = engine.getProperty('voice')


newVoiceRate = 100

engine.setProperty('rate', newVoiceRate,)
#engine.say('endet naw.')
engine.runAndWait()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Endamen ad eru!")

    elif hour >= 12 and hour < 18:
        speak("Endet walu !")

    else:
        speak("Endamen ameshu!")

    assname = (random.choice(["Seme yohana neaw","yohana ebala leu",]))

    speak(assname)


def usrname():

    speak(random.choice(['yen antas sim ','ye ersos sim']))
    uname = takeCommand()
    speak(random.choice(["Dis yemil sim neaw","Eshi","Sim temezgibal"]))

    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
    speak(random.choice(["endet lerdot?","min largalot","endet letazzez" ]))



def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("እያዳመጥኩ ነው...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("እያገናዘብኩ ነው...")
        query = r.recognize_google(audio, language='en-in')
        print(f"እንዳሉ: {query}\n")

    except Exception as e:
        print(e)
        print("አልተረዳሁም ?")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('ye email id', 'ye email passowrd')
    server.sendmail('your email id', to, content)
    server.close()


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    usrname()

    while True:

        query = takeCommand().lower()

        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            speak("youtube tekef tal\n")
            webbrowser.open("youtube.com")

        elif 'change voice' in query:
            speak('changing voice')
            engine.setProperty('voice now', voices[0].id)
            speak('This is my voice')
        elif 'google' in query:
            speak("google tekef tal\n")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif " music" in query or "play song's" in query or " song's" in query or "musica" in query:
            speak("musika tekef tal ")
            # music_dir = "G:\\Song"
            music_dir = "C:\\Users\\HP\\PycharmProjects\\Xion\\music"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            speak(f"Sir, the time is {strTime}")
        elif 'the Year' in query:
            strTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            speak(f"Sir, the year is {strTime}")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime(" %H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'the day' in query:
            strTime = datetime.datetime.now().strftime("  %A")
            speak(f"Sir, The day to day is after yesterday wha ha ha just jocking the day is {strTime}")

        elif 'email to gaurav' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Receiver email address"
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whome should i send")
                to = input()
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
        elif 'Listen' in query:
            speak("Sorry i can't here people who cant speak up!")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'peace' in query or "good" in query:
            speak("Hoo loom selam now")

        elif "change my name to" in query or "i don't like my name" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif 'exit' in query or 'by' in query:
            speak("By by")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Parallax ")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "calculate" in query:

            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who i am" in query:
            speak("You are who you want to be")

        elif "why you came to world" in query:
            speak("Thanks to Zemenu. further It's a secret")

        elif 'power point ' in query:
            speak("opening Power Point presentation")
            power = r"C:\\Users\\GAURAV\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
            os.startfile(power)

        elif "love"  in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Gaurav")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister Gaurav ")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed succesfully")

        elif 'open bluestack' in query:
            appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            os.startfile(appli)

        elif 'news' in query:

            try:
                jsonObj = urlopen(
                    '''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))


        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to me from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream=True)

            with open("Voice.py", "wb") as Pypdf:

                total_length = int(r.headers.get('content-length'))

                for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                       expected_size=(total_length / 1024) + 1):
                    if ch:
                        Pypdf.write(ch)

                        # NPPR9-FWDCX-D2C8J-H872K-2YT43
        elif "Fatima" in query:

            wishMe()
            speak(random.choice(["Fatima ebalalewn","Abet? "]))

            speak(assname)

        elif "weather" in query:

            # Google Open weather website
            # to get API of Open weather
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(
                    current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                    current_pressure) + "\n humidity (in percentage) = " + str(
                    current_humidiy) + "\n description = " + str(weather_description))

            else:
                speak(" City Not Found or do not exist you... idiot.....")

        elif " message " in query:
            # You need to create an account on Twilio to use this service
            account_sid = 'Account Sid key'
            auth_token = 'Auth token'
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                body=takeCommand(),
                from_='Sender No',
                to='Receiver No'
            )

            print(message.sid)

        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you Mister")
            speak(assname)

            # most asked question from google Assistant
        elif "Girlfriend" in query or "Boyfriend" in query:
            speak("Wait what NO!... You are a creep!")

        elif "how are you" in query or "hi" in query:
            speak("selam new ?")

        elif "Love" in query:
            speak("Love min malet new ?")


        elif "what is" in query or "who is" in query:

            # Use the same API key
            # that we have generated earlier
            client = wolframalpha.Client("API_ID")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")

                # elif "" in query:
            # Command go here
            # For adding more commands





