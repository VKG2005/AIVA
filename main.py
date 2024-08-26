import speech_recognition as sr
import os
import pyttsx3

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    print('pycharm')
    say("Hello, I am AIVA, your personal assistant")
