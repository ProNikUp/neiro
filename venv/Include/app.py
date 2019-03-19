import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3

def talk(words):
    enjine = pyttsx3.init()
    enjine.say(words)
    enjine.runAndWait()

talk("И л ю х а")