import speech_recognition as sr
import webbrowser
import win32com.client as wincl  # Native Windows voice
import time
import musicLibrary

# Initialize recognizer and Windows voice engine
recognizer = sr.Recognizer()
speaker = wincl.Dispatch("SAPI.SpVoice")

def speak(text):
    speaker.Speak(text)

def processCommand(c):
    c = c.lower()
    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")
    elif "open monkeytype" in c:
        speak("Opening Monkeytype")
        webbrowser.open("https://monkeytype.com/profile/SEE_Shashank")
    elif "open github" in c:
        speak("Opening GitHub")
        webbrowser.open("https://github.com/pythondeveloper483")
    elif c.startswith("play"):
        song = " ".join(c.split()[1:])  # handles multi-word songs
        if song in musicLibrary.music:
            speak(f"Playing {song}")
            link = musicLibrary.music[song]
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song.")
    elif "stop" in c:
        speak("Goodbye!")
        exit()

if __name__ == "__main__":
    speak("Initializing Jarvis... Please say 'Jarvis' to activate.")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
            word = recognizer.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yes, I am here.")
                time.sleep(1)  # ensure speech finishes before listening again

                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    print(f"Command: {command}")
                    processCommand(command)

        except Exception as e:
            print(f"Error: {e}")
