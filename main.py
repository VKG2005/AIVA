import datetime
import os
import subprocess
import webbrowser
import pyttsx3
import speech_recognition as sr
import pyaudio


def Guide(query):
    query = query.lower()
    if "hello" in query:
        say("welcome ! how may i help you .....")

    elif "help me please" in query:
        say("sure! i will ....")
        say("so I am going to give you some instructions for how to use me...")
        say("I am also going to display the following instructions ,"
            "so if you can't understand please refer that or feel free to ask me again....")

        say("instructions....")
        say("Here are the available tasks:")
        say("you have to give the instructions....")
        say("user instructions taken as input command for performinf tasks ")
        say("open websites....")
        say("open apps....")
        say("system volume adjustment....")
        say("manage files....")
        say("show  date and time... ")
        say("termination of program...")

        print("instructions....")
        print("Here are the available tasks:")
        print("open websites....")
        print("open apps")
        print("system volume adjustment")
        print("manage files")
        print("show  date and time ")
        print("termination of program...")


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
            print("recognizing....")
            query = r.recognize_google(audio, language="en-in")
            # query = r.recognize_google(audio, language="hi-in")
            print(f"User said: {query}")
        except Exception as e:
            print("Sorry, I didn't catch that. Could you please say that again?")
            return "none"
        return query


def open_websites(query):
    sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
             ["google", "https://www.google.com"],
             ["github", "https://github.com/VineshGoswami/AIVA"]]
    for site in sites:
        if f"open {site[0]}" in query.lower():
            say(f"opening {site[0]} sir......")
            webbrowser.open(site[1])


def open_App(query):
    if "open spotify" in query.lower():
        say("opening spotify sir......")
        subprocess.run(["start", "spotify:"], shell=True)
    elif "open whatsapp" in query.lower():
        say("opening whatsapp sir......")
        subprocess.run(["start", "whatsapp:"], shell=True)
    elif "open discord" in query.lower():
        say("opening discord sir ...")
        subprocess.run(["start", "discord:"], shell=True)
    elif "open linkedin" in query.lower():
        say("opening linkedIn sir.....")
        webbrowser.open("https://www.linkedin.com")


def volume_adjust(query):
    if "increase volume" in query:
        subprocess.run([r"C:\Users\vines\PycharmProjects\AIVA\nircmd-x64\nircmd.exe", "changesysvolume", "10000"])
        say("Volume increased sir")
    elif "decrease volume" in query:
        subprocess.run([r"C:\Users\vines\PycharmProjects\AIVA\nircmd-x64\nircmd.exe", "changesysvolume", "-10000"])
        say("Volume decreased sir")


def manage_files(query):
    if "open video" in query:
        videoPath = r"C:\Users\vines\New folder\WhatsApp Video 2024-08-19 at 19.47.56_5a11d9cd.mp4"
        say("opening file sir.....")
        os.startfile(videoPath)

    if "open pictures" in query:
        folderPath = "C:/Users/vines/OneDrive/Pictures"
        say("opening picture folder.sir....")
        os.startfile(folderPath)

    if "open documents" in query:
        doc_Path = r"C:\Users\vines\OneDrive\Pictures\Documents"
        say("opening document folder sir....")
        os.startfile(doc_Path)


def show_time():
    strfTime = datetime.datetime.now().strftime("%H:%M:%S")
    say("The current time is display on screen sir...")
    print("Current time:", strfTime)


def show_date():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    say("The current date is display on screen sir....")
    print("Current date:", current_date)


def chat(query):
    query = query.lower()
    if "how are you aiva" in query:
        say("I am fine sir, thank you for asking. How can I assist you today?")
        print("I am fine sir, thank you for asking. How can I assist you today?")

    elif "who is your boss" in query:

        say("Well, of course, you are! You brought me to life, ""after all. "
            "So, that makes you my brilliant creator ""and ultimate boss! "
            "What can I do for you today, boss?")

        print("Well, of course, you are! You brought me to life, after all. "
              "So, that makes you my brilliant creator and ultimate boss! "
              "What can I do for you today, boss?")

    elif "what you can do for me" in query:

        say("I can perform various tasks like opening apps, websites, adjusting volume, and more!")
        print("I can perform various tasks like opening apps, websites, adjusting volume, and more!")

    elif "thankyou" in query:

        say("You're welcome!")
        print("You're welcome!")


def input_numbers(query):
    query = query.lower()
    if "perform operations" in query:
        say("enter your variables  value sir ......")
        x = int(input("Enter variable1: "))
        print(f"First variable: {x}")
        say("enter the value of another variable sir.....")
        y = int(input("Enter variable2: "))
        print(f"Second variable: {y}")

        say("what operation you want to perform.......")
        operation = input("operation type +,-,*,%,** :").strip()
        result = None
        if operation == '+':
            result = x + y

        elif operation == '-':
            result = x - y

        elif operation == '*':
            result = x * y

        elif operation == '**':
            result = x ** y

        elif operation == '/':

            if y != 0:
                result = y/x
            else:
                say("number is not divided bu '0'")

        elif operation == '%':
            result = x % y
        else:
            say("Invalid operation selected.")
            return

        say(f"The result of {operation} operation on {x} and {y} is {result}.")
        print(f"Result: {result}")


def terminate(query):
    say("I am going to close this program. Thank you, sir.......")
    exit()


def main():
    say("Hey boss,how are you?,I am your personal assistant")

    while True:

        print('Listening....')
        #command for input from user
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

        chat(query)

        if "terminate the program" in query.lower():
            terminate(query)

        Guide(query)

        if "perform operations" in query.lower():
            input_numbers(query)


if __name__ == "__main__":
    main()
