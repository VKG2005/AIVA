AIVA - Personal Voice Assistant
Project Overview

AIVA (Artificially Intelligent Voice Assistant) is a Python-based voice-activated assistant that can handle various tasks, such as opening websites, apps, adjusting system volume, managing files, displaying date and time, and performing simple mathematical calculations.

The assistant interacts with the user through voice commands using the SpeechRecognition, pyttsx3, and Pyaudio libraries. It also provides text-based feedback for user convenience.
Features

    Voice Commands: Recognizes user voice commands using Google’s speech-to-text service.
    Opening Websites: Automatically opens popular websites like YouTube, Google, Wikipedia, and more.
    Opening Apps: Launches apps like Spotify, WhatsApp, Discord, and LinkedIn.
    System Volume Adjustment: Increases or decreases the system volume.
    File Management: Opens specified directories and files (documents, pictures, videos).
    Date and Time Display: Shows the current date and time upon request.
    Mathematical Operations: Performs arithmetic operations like addition, subtraction, multiplication, division, etc.
    Basic Chatting: Engages in simple conversations with the user.
    Program Termination: Allows for graceful termination of the program.

Prerequisites

To run AIVA, ensure that the following libraries are installed:

pip install pyttsx3
pip install SpeechRecognition
pip install pyaudio


Running the Program:

    Make sure you have a working microphone connected to your system.
    Run the program using

    Interacting with AIVA:
        Give voice commands like:
            "Open YouTube"
            "Open Spotify"
            "Increase volume"
            "What is the time?"
            "Perform operations" (for math calculations)
        AIVA will respond both by speaking and showing output on the console.

Instructions

When asking for help, AIVA provides the following instructions:

    You can open websites by saying "Open [website name]".
    You can open apps by saying "Open [app name]".
    Control the system volume using commands like "Increase volume" or "Decrease volume".
    Ask for the current date and time with "What is the date?" or "What is the time?"
    Perform basic math operations by saying "Perform operations".
    Terminate the program by saying "Terminate the program".

Example Commands

    Open YouTube: "Open YouTube"
    Open App: "Open Spotify"
    Show Date: "What is the date?"
    Perform Calculations: "Perform operations" (Then follow the prompts for input)
    Terminate: "Terminate the program"

Libraries Used

    datetime – For getting the current date and time.
    os – For file handling operations.
    subprocess – For opening apps and controlling system processes.
    webbrowser – For opening websites.
    pyttsx3 – Text-to-speech conversion for voice responses.
    speech_recognition – For recognizing and processing voice input.
    pyaudio – To interact with the system microphone.

Future Improvements

    Add more commands: Include additional functionalities like sending emails, weather updates, etc.
    Improve error handling: Make the assistant more robust against misinterpretations.
    Custom voice models: Add support for custom-trained voice recognition models.
