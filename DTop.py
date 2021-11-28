import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

from wikipedia import exceptions

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Geeva Sir... Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('projects.sg001@gmail.com', 'arjun#31')
    server.sendmail('projects.sg001@gmail.com', to, content)
    server.close()

command = True

if __name__ == "__main__":
    wishMe()
    while command:
        query = takeCommand().lower()
        
        #logic for executing tasks based on query

        if 'wikipedia' in query:
            speak("Searching wikipedia sir...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com//")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open myntra' in query:
            webbrowser.open("myntra.com")

        elif 'open amazon' in query:
            webbrowser.open("amazon.com")

        elif 'open book my show' in query:
            webbrowser.open("bookmyshow.com")

        elif 'play music' in query:
            music_dir = 'D:\\songs\\favourites'
            songs = os.listdir(music_dir)
            print(songs)
            #speak("Which song should I play sir...")
            #playSong = takeCommand()
            #song = songs.index(playSong)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'the code' in query:
            codePath = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to shraddha' in query:
            try:
                speak("What should I say, sir...")
                content = takeCommand()
                to = "projects.sg001@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry sir... I am not able to send this mail")
        
        elif 'thank you' in query:
            speak("My pleasure sir...")
        
        elif 'quit' in query:
            speak("Thank you sir... for having me. Have a good day sir")
            command = False

        elif 'shutdown' in query:
            speak("Thank you sir... for having me. Have a good day sir")
            command = False

        elif '' in query:
            print("")
       
        else:
            speak("Sorry Sir... I cannot perform this command. I will work on it in future")



