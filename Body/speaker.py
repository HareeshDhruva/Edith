#windows based
from multiprocessing.connection import wait
from time import sleep
#from typing import dataclass_transform
from webbrowser import Chrome
import pyttsx3

def speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    engine.setProperty('rate',170)
    print(f"you : {Text}.")
    print("")
    engine.say(Text)
    data = engine.runAndWait()
    return data

