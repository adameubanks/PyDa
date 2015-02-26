import wx
from datetime import datetime
from espeak import espeak
from time import sleep
import string
import re

now = datetime.now()
hour = now.hour
if hour < 12:#am
    espeak.synth("Good morning, what can I help you with?")
if hour == 12:
    espeak.synth("Good day, what can I help you with?")
if hour > 12:#5 pm
    if hour <= 18:
        espeak.synth("Good afternoon, what can I help you with?")
    if hour > 18:
        espeak.synth("Good evening, what can I help you with?")


class MyFrame(wx.Frame):
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN, 
            title="PyDa")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
                            label="Hello I am Pyda the Python Digital Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        favicon = wx.Icon('Pyda.ico', wx.BITMAP_TYPE_ICO, 16, 16)
        wx.Frame.SetIcon(self, favicon)
        
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
    
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()
    #--------------------------Pyda Function-------------------------------------------
    
    def OnEnter(self, event):
        import webbrowser
        import os
        
        input = self.txt.GetValue()
        input = input.lower()

        #the variables
        time = ["hour","day","month","year"]
        insults = ["weirdo" , "stupid" , "weird" , "dumb" , "idiot" , "retard" , "retarded" , "fat" , "lazy" , 
        "annoying" , "moron" , "simp" ,"big" , "ugly" , "sad" , "wimp"]
        complements = ["nice","happy","good","smart","wonderful","really ","intellegent","awesome","beautiful"]

        #generate randNum
        from random import randrange
        ranNum = randrange(1,4)
        #chatting features of PyDa:
        if input.startswith("do you want to "):
            if ranNum == 1:
                espeak.synth("Maybe later")
            if ranNum == 2:
                espeak.synth("I don't think thats a good idea")
            if ranNum == 3:
                espeak.synth("Yes! lets do it")
        if input.startswith("do you like to "):
            if ranNum == 1:
                espeak.synth("Sometimes I do")
            if ranNum == 2:
                espeak.synth("No, I hate doing that")
            if ranNum == 3:
                espeak.synth("Yes, I do that all the time")
        if input.startswith("i hate "):
            if 'khanrad' in input[6:]:
                espeak.synth("What? khanrad is the coolest person ever!")
            elif ranNum > 2:
                espeak.synth("I think "+input[6:]+" is awesome")
            elif ranNum <= 2:
                espeak.synth("I don't like "+input[6:]+' either')

        if input.startswith("you are a"):
            if any(input[7:].startswith(c) for c in complements):
                if ranNum == 1:
                    espeak.synth("Thank you, I know")
                if ranNum == 2:
                    espeak.synth("isn't it obvious?")
                if ranNum == 3:
                    espeak.synth("you made my day!")
            if any(input[7:].startswith(i) for i in insults):
                if ranNum == 1:
                    espeak.synth("I know you are but what am i?")
                if ranNum == 2:
                    espeak.synth("You are a troll. I eat trolls")
                if ranNum == 3:
                    espeak.synth("sorry, i was to busy, BLOCKING OUT THE HATERS!")
            else:
                if ranNum == 1:
                    espeak.synth("I don't know what you mean by that")
                if ranNum == 2:
                    espeak.synth("Your words are not in my library")
                if ranNum == 3:
                    espeak.synth("No comment")

        if input.startswith("are you a"):
            if any(input[7:].startswith(c) for c in complements):
                if ranNum == 1:
                    espeak.synth("of course I am")
                if ranNum == 2:
                    espeak.synth("isn't it obvious?")
                if ranNum == 3:
                    espeak.synth("you betcha")
            if any(input[7:].startswith(i) for i in insults):
                if ranNum == 1:
                    espeak.synth("No, no I'm not")
                if ranNum == 2:
                    espeak.synth("You are a troll. I eat trolls")
                if ranNum == 3:
                    espeak.synth("I cant even")
            else:
                if ranNum == 1:
                    espeak.synth("I don't know what that is")
                if ranNum == 2:
                    espeak.synth("Your words are not in my library")
                if ranNum == 3:
                    espeak.synth("No comment")

        #webbrowser openers
        if "mail" in input:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            espeak.synth("opening your gmail")
        if "search" in input:
            webbrowser.open("http://www.google.com")
            espeak.synth("opening google")
        if "facebook" in input:
            webbrowser.open("https://www.facebook.com/")
            espeak.synth("openning facebook")
        if "twitter" in input:
            webbrowser.open("https://twitter.com/")
            espeak.synth("opening twitter")
        if "youtube" in input:
            webbrowser.open("https://www.youtube.com/")
            espeak.synth("opening youtube")
        #Time commands
        if "time" in input:
            import pynotify
            from time import gmtime, strftime
            pynotify.init("Date Time")
            time = pynotify.Notification(strftime("%a, %d %b %Y %H:%M ",gmtime()))
            time.show()

        if "count" in input:
            usrCount = int(''.join(ele for ele in input if ele.isdigit()))
            for x in range (1, int(usrCount)+1):
                espeak.synth(str(x))
                if x == int(usrCount):
                    espeak.synth("Time's Up!")
                    print "Time's Up!"
                if 1==1:
                    sleep(1)

        #os commands
        if "web" in input:
            os.system("firefox")
        if "logout" in input:
            espeak.synth("Logging out")
            os.system("gnome-session-quit")
        if "music" in input:
            espeak.synth("playing music")
            os.system("rhythmbox")
        if "skype" in input:
            espeak.synth("opening skype")
            os.system("skype")
        if "text" in input:
            espeak.synth("opening get it")
            os.system("gedit")
        if "math" in input:
            espeak.synth("opening calculator")
            os.system("gnome-calculator")
        '''Exiting PyDa'''
        if  "quit" in input:
            espeak.synth("goodbye")
            sleep(1)
            quit()

        #system questions
        if "battery" in input:
            import commands
            import pynotify
            from threading import Timer
            def battery_check():
                rem = float(commands.getoutput("grep \"^remaining capacity\" /proc/acpi/battery/BAT1/state | awk '{ print $3 }'"))
                full = float(commands.getoutput("grep \"^last full capacity\" /proc/acpi/battery/BAT1/info | awk '{ print $4 }'"))
                state = commands.getoutput("grep \"^charging state\" /proc/acpi/battery/BAT1/state | awk '{ print $3 }'")
                 
                percentage = int((rem/full) * 100)
             
                if state == "discharging":
                    pynotify.init("Battery Alert!")
                    notification = pynotify.Notification("Battery "+state,str(percentage)+"%",
                        "/usr/share/icons/gnome/32x32/status/battery-low.png")
                    notification.show()
                    espeak.synth("Your battery is "+state+"at"+str(percentage)+"percent")
                    timer = Timer(9999999999999999.9,battery_check)
                    timer.start()
            if __name__ == "__main__":
                battery_check()


        #Math

        if '+' in input:
            find_add = input.find('+')
            resultAdd = str(float(input[:find_add]) + float(input[find_add+1:]))
            print resultAdd
            espeak.synth(resultAdd)

        if '-' in input:
            find_sub = input.find('-')
            resultSub = str(float(input[:find_sub]) - float(input[find_sub+1:]))
            print resultSub
            espeak.synth(resultSub)

        if '*' in input:
            find_mul = input.find('*')
            resultMul = str(float(input[:find_mul]) * float(input[find_mul+1:]))
            print resultMul
            espeak.synth(resultMul)

        if '/' in input:
            find_div = input.find('/')
            resultDiv = str(float(input[:find_div]) / float(input[find_div+1:]))
            print resultDiv
            espeak.synth(resultDiv)
        if '%' in input:
            find_mod = input.find('%')
            resultMod = str(float(input[:find_mod]) % float(input[find_mod+1:]))
            print resultMod
            espeak.synth(resultMod)

        #Info from Wikipedia
        import wikipedia
        if input.startswith('look up'):
            wikiLookUp = input[7:]
            print "Searched for: "+wikiLookUp
            espeak.synth("Searched for: "+wikiLookUp)
            print wikipedia.summary(wikiLookUp)

        if input.startswith('who is '):
            wikiLookUp = input[7:]
            print "Searched for: "+wikiLookUp
            espeak.synth("Searched for: "+wikiLookUp)
            print wikipedia.summary(wikiLookUp)

        if input.startswith('who was '):
            wikiLookUp = input[8:]
            print "Searched for: "+wikiLookUp
            espeak.synth("Searched for: "+wikiLookUp)
            print wikipedia.summary(wikiLookUp)

        if input.startswith('what is '):
            wikiLookUp = input[8:]
            print "Searched for: "+wikiLookUp
            espeak.synth("Searched for: "+wikiLookUp)
            print wikipedia.summary(wikiLookUp)

        if input.startswith('where is '):
            wikiLookUp = input[9:]
            print "Searched for: "+wikiLookUp
            espeak.synth("Searched for: "+wikiLookUp)
            print wikipedia.summary(wikiLookUp)

        '''Translate'''

        if input.startswith("translate "):
            import goslate
            gs = goslate.Goslate()

            trans = input[10:-6]
            lang = input[-2:]
            print 'Translated: '+trans+' into '+lang
            print gs.translate(trans , lang)
        if 'languages' in input:
            print "I know 90 languages:  use the languages below and there key to translate: "
            espeak.synth("I know 90 languages")
            print gs.get_languages()

        '''Speech Recognition'''
        if input == '':
            import speech_recognition as sr
            r = sr.Recognizer()
            with sr.Microphone() as source:                # use the default microphone as the audio source
                audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

            try:
                self.txt.SetValue(r.recognize(audio))
                    
            except LookupError:                            # speech is unintelligible
                print("Could not understand audio")


            

if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
