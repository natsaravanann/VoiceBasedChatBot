import speech_recognition as sr
import gtts
import time
from time import ctime
import playsound
import webbrowser
import random
import os
def record_audio(ask=False):
    r=sr.Recognizer()
    r.energy_threshold = 6000
    voicedata=''
    if ask:
        simplyspeak(ask)
    try:
        with sr.Microphone() as source:
            audio=r.listen(source)
            voicedata=r.recognize_google(audio,language='en-US')            
    except sr.UnknownValueError:
        print("Unable to Recognize Audio")
    except sr.RequestError:
        print("Unable to find the Resource")
    return voicedata
def simplyspeak(stringdata):
    print(stringdata)
    tts=gtts.gTTS(text=stringdata,lang='en')
    r=random.randint(1,100000)
    audiofile="audio-"+str(r)+".mp3"
    tts.save(audiofile)
    playsound.playsound(audiofile)
    os.remove(audiofile)
def respond(query):
    s1=["my name","name of mine"]
    s2=["your name","name of yours"]
    s3=['close','stop','exit']
    if  (s1[0]  in query) or (s1[1] in query):
        name=record_audio(ask="Speak out your name loudly")
        simplyspeak("Your name is "+str(name))
    elif (s2[0]  in query) or (s2[1] in query):
        name="Google Assistant"
        simplyspeak("My name is "+str(name))
    elif ("master" in query) or ("chief" in query):
        simplyspeak("My master's name is Saravanan Natarajan")
    elif "time" in query:
        simplyspeak(ctime())
    elif ("search" in query) or ("find" in query):
        search=record_audio(ask="what do you want to search for?")
        url="https://google.com/search?q="+str(search)
        webbrowser.get().open(url)
        simplyspeak("Your search for "+str(search)+" is opened here")        
    elif ("stop" in query) or ("close" in query) or ("exit" in query):
        simplyspeak("I am Exiting")
        exit()
while True:
    simplyspeak("How can I help You?")
    query=record_audio()
    respond(query)
