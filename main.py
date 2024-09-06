import datetime
import os
import subprocess
import webbrowser
import pyttsx3
import speech_recognition as sr
import pyaudio


def say(text):
    print(f"Speaking: {text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def input_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1

        audio = r.listen(source)

        try:
            print ("recognizing....")
            query = r.recognize_google(audio, language="en-in")
            # query = r.recognize_google(audio, language="hi-in")
            print(f"User said: {query}")
        except Exception as e:
            print("Sorry, I didn't catch that. Could you please say that again?")
            return "none"
        return query

def volume_adjust(query):
    if "increase volume" in query:
        subprocess.run([r"C:\Users\vines\PycharmProjects\AIVA\nircmd-x64\nircmd.exe", "changesysvolume", "10000"])
        say("Volume increased")
    elif "decrease volume" in query:
        subprocess.run([r"C:\Users\vines\PycharmProjects\AIVA\nircmd-x64\nircmd.exe", "changesysvolume", "-10000"])
        say("Volume decreased")

def main():
    say("Hey boss,how are you?,I am your personal assistant")
    while True:
        print('Listening....')
        query = input_command()
        if query == 'none':
            continue
        volume_adjust(query)




if __name__ == "__main__":
    main()

