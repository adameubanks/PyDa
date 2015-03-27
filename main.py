import wx
from datetime import datetime
from espeak import espeak

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
        
        input = self.txt.GetValue()
        input = input.lower()  

        from chat import chat
        chat(input)

        from operations import oper
        oper(input)

        from mathOper import math
        math(input)
        
        from lookup import lookup
        lookup(input)

        from translate import translate
        translate(input)


        if 'help' in input:
            with open('help.txt', 'r') as fin:
                print fin.read()        


        #-----------Speech Recognition----------#
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
