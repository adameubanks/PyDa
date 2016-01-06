from espeak import espeak
import webbrowser
import os
from datetime import datetime
from time import sleep

def oper(input):
    #webrowser openners
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
