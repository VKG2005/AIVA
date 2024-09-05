import speech_recognition as sr
import os
import pyttsx3
import pyaudio
import webbrowser


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def input_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:  # Fixed typo here
        r.pause_threshold = 1

        audio = r.listen(source)

        try:
            print ("recognizing....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
        except Exception as e:
            print("Sorry, I didn't catch that. Could you please say that again?")
            return "none"
        return query


if __name__ == "__main__":
    print('Pycharm')
    say("Hello, I am AIVA, your personal assistant")
    while True:
        print('Listening....')
        query = input_command()

        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"], ["spotify", "spotify:"] ,["whatsapp" ,"whatsapp:"]]
        for site in sites:
            if f"open {site[0]}" in query.lower():
                say(f"Opening {site[0]} sir....")
                webbrowser.open(site[1])
                break

        if site[0] == "spotify":
            say("Opening Spotify...")
            break

        if site[0] == "whatsapp":
            say("opening whatsapp........")
            break

        if "open video" in query:
            videoPath = r"C:\Users\vines\New folder\WhatsApp Video 2024-08-19 at 19.47.56_5a11d9cd.mp4"
            os.startfile(videoPath)
            break

        if "open pictures" in query:
            folderPath = "C:/Users/vines/OneDrive/Pictures"
            os.startfile(folderPath)
            break
