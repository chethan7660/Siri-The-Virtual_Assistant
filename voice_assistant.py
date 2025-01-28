import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import pyjokes  # pip install pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 180)  # Speed of speech
engine.setProperty('volume', 0.9)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Siri. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I'm listening...")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        speak("1 second")
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print(f"Error fetching Wikipedia results: {e}")
                speak("I could not find any information on that.")

        elif 'open youtube' in query:
            speak("What should I search on YouTube?")
            search_query = takeCommand().lower()
            if search_query != "none":
                webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
                speak(f"Here are the results for {search_query} on YouTube.")

        elif 'open google' in query:
            speak("What should I search on Google?")
            search_query = takeCommand().lower()
            if search_query != "none":
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
                speak(f"Here are the results for {search_query} on Google.")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\CHETHAN\\Music\\songs'  # Update with your music folder path
            try:
                songs = os.listdir(music_dir)
                if songs:
                    print(songs)
                    os.startfile(os.path.join(music_dir, songs[0]))
                    speak("Playing music from your collection.")
                else:
                    speak("Your music folder is empty.")
            except FileNotFoundError:
                speak("Music directory not found. Please update the path.")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open vscode' in query:
            codePath = "C:\\Users\\CHETHAN\\Downloads\\VSCodeUserSetup-x64-1.91.1\\Code.exe"
            if os.path.exists(codePath):
                os.startfile(codePath)
                speak("Opening Visual Studio Code.")
            else:
                speak("Visual Studio Code is not installed or the path is incorrect.")

        elif 'open file manager' in query:
            os.startfile("C:\\")  # Opens the root directory
            speak("Opening File Manager.")

        elif 'open gallery' in query:
            gallery_dir = "C:\\Users\\CHETHAN\\Pictures\\gallery"  # Update with your gallery path
            if os.path.exists(gallery_dir):
                os.startfile(gallery_dir)
                speak("Opening gallery.")
            else:
                speak("Gallery folder does not exist.")
        
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif 'exit' in query:
            speak("Goodbye! Have a great day!")
            print("Exiting program...")
            break
