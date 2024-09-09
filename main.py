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


def open_websites(query):
   sites = [["youtube","https://www.youtube.com"],["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],
            ["github","https://github.com/VineshGoswami/AIVA"]]
   for site in sites:
       if f"open {site[0]}" in query.lower():
           say(f"opening {site[0]} sir......")
           webbrowser.open(site[1])


def open_App(query):
    if "open spotify" in query.lower():
        say("opening spotify ......")
        subprocess.run(["start","spotify:"], shell=True)
    elif "open whatsapp" in query.lower():
        say("opening whatsapp......")
        subprocess.run(["start","whatsapp:"], shell=True)
    elif "open discord" in query.lower():
        say("opening discord...")
        subprocess.run(["start","discord:"], shell=True)
    elif "open linkedin" in query.lower():
        say("opening linkedIn.....")
        webbrowser.open("https://www.linkedin.com")


def volume_adjust(query):
    if "increase volume" in query:
        subprocess.run([r"C:\Users\vines\PycharmProjects\AIVA\nircmd-x64\nircmd.exe", "changesysvolume", "10000"])
        say("Volume increased")
    elif "decrease volume" in query:
        subprocess.run([r"C:\Users\vines\PycharmProjects\AIVA\nircmd-x64\nircmd.exe", "changesysvolume", "-10000"])
        say("Volume decreased")


def manage_files(query):

    if "open video" in query:
        videoPath = r"C:\Users\vines\New folder\WhatsApp Video 2024-08-19 at 19.47.56_5a11d9cd.mp4"
        say("opening file.....")
        os.startfile(videoPath)

    if "open pictures" in query:
        folderPath = "C:/Users/vines/OneDrive/Pictures"
        say("opening picture folder.....")
        os.startfile(folderPath)

    if "open documents" in query:
        doc_Path = r"C:\Users\vines\OneDrive\Pictures\Documents"
        say("opening document folder....")
        os.startfile(doc_Path)


def show_time():
    strfTime = datetime.datetime.now().strftime("%H:%M:%S")
    print("Current time:", strfTime)


def show_date():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    print("Current date:", current_date)


def terminate(query):
    say("I am going to close this program. Thank you, sir.......")
    exit()


def main():
    say("Hey boss,how are you?,I am your personal assistant")
    while True:
        print('Listening....')
        query = input_command()
        if query == 'none':
            continue
        open_websites(query)
        open_App(query)
        volume_adjust(query)
        manage_files(query)
        if "time" in query:
            show_date()
        if "date" in query:
            show_time()
        if "terminate the program" in query.lower():
            terminate(query)
g

if __name__ == "__main__":
    main()