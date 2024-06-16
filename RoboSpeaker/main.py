import os
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by Shashank Goyal")
    while(True):
        s = input("Enter what to Speak : ")
        if s=="q":
           speaker.Speak("bye bye my friend")
           break
        speaker.Speak(s)