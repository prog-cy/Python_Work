import pyttsx3
import time
engine = pyttsx3.init()
engine.say("This is a program for speech. And your can understand the power of computer.")

time.sleep(2)
engine.say("You have waited for 2 second and then you are saying second line")
engine.runAndWait()