import pyttsx3,datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Im Jarvis .. How can I Help You?")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold= 1
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print("You Said : ",query)

    except Exception as e:
        print("Say that again please....")
        return 'None'

    return query




if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        
        
        if "wikipedia" in query:
            speak("Searching wikipedia....")
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia...")
            print(results)
            speak(results)
            

        elif 'open youtube' in query:
            query=query.replace('open',"")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            query=query.replace('open',"")
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            query=query.replace('open',"")
            webbrowser.open("youtube.com")

        elif 'play music' in query:
            pass

        elif 'tell time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak("The Time is")
            speak(strTime)
            
        elif 'open code' in query:
            codepath="C:\\Users\\rahul\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open firefox' in query:
            path1="C:\Program Files\Mozilla Firefox\firefox.exe"
            os.startfile(path1)

        elif 'open chrome' in query:
            path2="C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(path2)

        elif 'open setting' in query:
            path3="%windir%\System32\Control.exe"
            os.startfile(path3)

        elif 'open bluestacks' in query:
            path4="C:\Program Files\BlueStacks_nxt\HD-Player.exe --instance Nougat32"
            os.startfile(path4)

            
