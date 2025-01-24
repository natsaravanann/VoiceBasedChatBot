import speech_recognition as sr
import time
import gtts
import playsound
import random
import os
import webbrowser
from tkinter import *
import threading
import time
class SpeechRecognizer(threading.Thread):
    def __init__(self):
         super(SpeechRecognizer, self).__init__()
         self.setDaemon(True)
         self.query= " "
         self.answer=" "
    def respond(self,query):
        ans=""
        x =["close","stop","exit"]
        if query.lower() in x:
            self.simplyspeak("I am exiting")
            ans="I am exiting"
            root.destroy()
            exit()
        elif "your name" in query.lower():
            self.simplyspeak("My name is Google Assistant")
            ans="My name is Google Assistant"
        elif "my name" in query.lower():
            #self.simplyspeak("My name is Google Assistant")
            ans="Please Speak out Your name loudly"
            name= self.recordaudio(ask=ans)
            ans="Your name is "+ name
            self.simplyspeak(ans)
        elif "what do you think of me" in query.lower():
            self.simplyspeak("You are the most smartest intelligent and nice person I have ever met")
            ans="You are the most smartest intelligent and nice person I have ever met"
        elif "who is your master" in query.lower() or "what is your master's name" in query.lower():
            self.simplyspeak("My master's name is Saravanan Natarajan")
            ans="My master's name is Saravanan Natarajan"
        elif "find" in query.lower() or "search" in query.lower():
            ans="What do you want to search?"
            search= self.recordaudio(ask="What do you want to search?")
            url="https://google.com/search?q="+search
            webbrowser.get().open(url)
            ans="What You Searched for "+search+" is here.."
            self.simplyspeak(ans)
            
        elif ("open word" in query.lower()):
            ans="opening Microsoft Word"
            self.simplyspeak(ans)
            os.startfile("winword.exe")
            
        elif ("open powerpoint" in query.lower()):
            ans="opening Microsoft powerpoint"
            self.simplyspeak(ans)
            os.startfile("powerpnt.exe")
        elif ("open excel" in query.lower()) or ("open microsoft excel" in query.lower()) :
            ans="Opening Microsoft Excel"
            self.simplyspeak(ans)
            os.startfile("excel.exe")
        elif ("open notepad" in query.lower()):
            ans="Opening Notepad"
            self.simplyspeak(ans)
            os.startfile("notepad.exe")
        else:
            self.simplyspeak("I didn't understand What you said now quoted "+query)
            ans="I didn't understand What you said now quoted "+query
            pass
        return ans
    def recordaudio(self,ask=False):
        r=sr.Recognizer()
        r.energy_threshold=6000
        voicetext=''
        if ask:
            #ans=ask
            self.simplyspeak(ask)
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source,1.2)
                audio=r.listen(source)
                voicetext=r.recognize_google(audio,language="en-IN")
                #print(voicetext)
        except sr.UnknownValueError:
            self.simplyspeak("Unable to recognize the audio")
        except sr.RequestError:
            self.simplyspeak("Unable to produce result")
        return voicetext
    def simplyspeak(self,strdata):
        #print(strdata)
        tts=gtts.gTTS(text=strdata,lang="en")
        audiofile="audio-"+str(random.randint(1,10000))+".mp3"
        tts.save(audiofile)
        playsound.playsound(audiofile)
        os.remove(audiofile)
    def run(self):
        while True:
            time.sleep(1)
            self.answer="How can  I help You?"
            self.simplyspeak("How can  I help You?")
            self.query=self.recordaudio()
            self.answer=self.respond(self.query)
recognizer = SpeechRecognizer()
recognizer.start()

class App(object):
    def __init__(self,root):
        self.root = root
        txt_frm = Frame(self.root, width=450, height=180)
        txt_frm.pack(fill="both", expand=True)
         # ensure a consistent GUI size
        txt_frm.grid_propagate(False)
        self.titlelabel1=Label(txt_frm,text="               Speak-to-it Assistant in English             ",fg="dark blue",font = "Helvetica 16 bold")
     # create first Text label, widget and scrollbar
        #self.lbl1 = Label(txt_frm, text="Type")
        self.titlelabel1.grid(row=0,column=0,columnspan=100,sticky=W)

        self.query= StringVar()
        self.txt1 = Text(txt_frm, borderwidth=3, relief="sunken", height=4,width=55)
        self.txt1.grid(row=50, column=7, sticky="nsew", padx=2, pady=2)
        self.answer = StringVar()
        self.txt2 = Text(txt_frm, borderwidth=3, relief="sunken", height=4,width=55)
        self.txt2.grid(row=25, column=7, sticky="nsew", padx=2, pady=2)
        root.after(100, self.update_recognized_text)

    def update_recognized_text(self):
        #print(recognizer.answer)
        #print(recognizer.query)
        self.txt1.delete(0.0, END)
        self.txt1.insert(0.0, recognizer.query)
        self.txt2.delete(0.0, END)
        self.txt2.insert(0.0, recognizer.answer)
        root.after(100, self.update_recognized_text)

    

root = Tk()
app = App(root)
root.title("Digital Assistant in English")
root.iconbitmap('file.ico')
root.mainloop()
        

