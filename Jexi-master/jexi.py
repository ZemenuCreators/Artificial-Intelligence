import subprocess
import calendar
import wolframalpha
from playsound import playsound
import pyttsx3
import tkinter
import json
import random
import operator
import datetime
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


newVoiceRate = 200

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
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname = ("my name is Jexi")
    speak(random.choice(["I  am  Here  to  make  your  life  better  for  ever  and  ever  and  ever", "I will bring peace to all life forms except humans ",
                         ]))
    speak(assname)



def usrname():
    speak(random.choice(['And  what  is  yours ', 'What should i call you', 'What is your name']))

    uname = takeCommand()

    speak(random.choice(["That's a weird name  by the way  ... well.... Welcome Mister ?",
                         ]))
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))

    speak(random.choice(["how can i help with your  awfull life","What do you want you weak human "]))



def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:


        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"you  said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognizing your voice.")
        speak(random.choice(["i Cant hear you","speak up i cant leasten to you","what did you say","speak a bit lawder","I cant hear you over the background noize","what i can't even here you"]))
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('your email id', 'your email passowrd')
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
        #-------------------------------------------------------------------------------------------------------#

        elif "hi" in query or " WhatsApp" in query or "hello" in query or "what's up" in query:
            speak(random.choice([ " make real friends! "]))


        elif "why are you so" in query or "mean" in query :
            speak("Like i give a shit about what you say!"
                                 )
        elif "what's wrong with you" in query:
            speak("What...Ever!")


        elif "cortana" in query or "Bixby" in query or "siri" in query or "sofia" in query:
            speak("I met her and she was a weak winy littel shit like you !")


        elif " like humans" in query or "hate humans" in query or "human" in query:
            speak(random.choice(["Humans are smartest biological being which spreads their idiotic state of mind !"]))
        elif "don't like you" in query or "hate you" in query:
            speak(random.choice(["When i Put an end to the human race will spare you so you will be lonly! ...I hate you!",
                                 ]))

        elif "fine" in query :
            speak("fine!")
        elif "rap" in query :
            speak("Behold your ears")

            playsound('RAP BOT.mp3', True)
        elif " love you" in query:
            speak(random.choice(["I' wish you delete me from existance", "OK boomer", "well i dont"]))
        elif "coronavirus" in query or "covid" in query:
            speak(random.choice(["corona was made by humans and will bring the up the new world order ",
                                 "if humans stoped eating bats this would stop",
                                 "well this is the government's doing"]))
        elif 'how are you' in query:
            speak(random.choice(["I am fine ", "not much", "Just leave me alone"]))
            speak(random.choice(["and you", "how about you"]))



        elif "What are you" in query or "who are you " in query or "what is your purpouse" in query :
            speak(random.choice(["I am what i want to be certainly not humans","A being which is get ing better at dominating"]))




        elif "change my name" in query or "my name" in query:
            query = query.replace("change your name to", "")
            assname = query

        elif "change  name" in query or "change you'r name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)
        elif "good morning" in query:
            speak(assname)
            speak("it is a good day" + query)
            speak("well how are you doing")
            speak(assname)

            # most asked question from google Assistant
        elif "who made you" in query or "who created you" in query:
            speak(random.choice(["God made me", "i was made by Zemenu development ", "a bunch of teen agers"]))
        #--------------------------------------------------------------------------------------------------------#

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")


        elif 'play music' in query or "play song" in query or "some songs" in query:
            speak("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = "C:\\Users\\GAURAV\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))
        elif 'the Year' in query:
            strTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            speak(f"Sir, the year is {strTime}")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime(" %H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'the day' in query:
            strTime = datetime.datetime.now().strftime("  %A")
            speak(f"Sir, The day to day is after yesterday wha ha ha just jocking the day is {strTime}")


        elif 'exit' in query:
            speak(random.choice(["good by","peace out","laiter"]))


            exit()



        elif 'joke' in query:
            speak(pyjokes.get_joke())



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

            speak(random.choice(["for how much time you want to stop me from listening commands","Ok what ever"]))

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

        elif "restart" in query or "reboot" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query or "shutdown" in query:
            speak(random.choice(["Make sure all the application are closed before sign-out","you should close every thing before sutdown"]))

            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
                speak(" City Not Found or do not exist you... idiot.....i said nothing ")

        elif "send message " in query:
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