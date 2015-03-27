from espeak import espeak

def chat(input):
    insults = ["weirdo" , "stupid" , "weird" , "dumb" , "idiot" , "retard" , "retarded" , "fat" , "lazy" , 
    "annoying" , "moron" , "simp" ,"big" , "ugly" , "sad" , "wimp","troll"]
    complements = ["nice","happy","good","smart","wonderful","really ","intellegent","awesome","beautiful"]
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

    words = input.split

    if input.startswith("you are a"):
        if any(input[10:].startswith(c) for c in complements):
            if ranNum == 1:
                espeak.synth("Thank you, I know")
            if ranNum == 2:
                espeak.synth("isn't it obvious?")
            if ranNum == 3:
                espeak.synth("you made my day!")
        elif any(input[11:].startswith(c) for c in complements):
            if ranNum == 1:
                espeak.synth("Thank you, I know")
            if ranNum == 2:
                espeak.synth("isn't it obvious?")
            if ranNum == 3:
                espeak.synth("you made my day!")
        
        if any(input[10:].startswith(i) for i in insults):
            if ranNum == 1:
                espeak.synth("I know you are but what am i?")
            if ranNum == 2:
                espeak.synth("Don't troll me. bad things will happen")
            if ranNum == 3:
                espeak.synth("sorry, i was to busy, BLOCKING OUT THE HATERS!")
        elif any(input[11:].startswith(i) for i in insults):
            if ranNum == 1:
                espeak.synth("I know you are but what am i?")
            if ranNum == 2:
                espeak.synth("Don't troll me. bad things will happen")
            if ranNum == 3:
                espeak.synth("sorry, i was to busy, BLOCKING OUT THE HATERS!")
        
        elif input[10:] or input[11:] not in insults:
            if ranNum == 1:
                espeak.synth("I don't know what you mean by that")
            if ranNum == 2:
                espeak.synth("Your words are not in my library")
            if ranNum == 3:
                espeak.synth("No comment")
        elif input[10:] or input[11:] not in complements:
            if ranNum == 1:
                espeak.synth("I don't know what you mean by that")
            if ranNum == 2:
                espeak.synth("Your words are not in my library")
            if ranNum == 3:
                espeak.synth("No comment")


    if input.startswith("are you a"):
        if any(input[10:].startswith(c) for c in complements):
            if ranNum == 1:
                espeak.synth("yes i am")
            if ranNum == 2:
                espeak.synth("isn't it obvious?")
            if ranNum == 3:
                espeak.synth("you betcha")
        elif any(input[11:].startswith(c) for c in complements):
            if ranNum == 1:
                espeak.synth("yes i am")
            if ranNum == 2:
                espeak.synth("isn't it obvious?")
            if ranNum == 3:
                espeak.synth("you betcha")

        if any(input[10:].startswith(i) for i in insults):
            if ranNum == 1:
                espeak.synth("no, are you")
            if ranNum == 2:
                espeak.synth("don't troll me, i eat trolls")
            if ranNum == 3:
                espeak.synth("does it look like i am?")
        elif any(input[11:].startswith(i) for i in insults):
            if ranNum == 1:
                espeak.synth("no, are you")
            if ranNum == 2:
                espeak.synth("don't troll me, i eat trolls")
            if ranNum == 3:
                espeak.synth("does it look like i am?")
        
        elif input[10:] or input[11:] not in insults or complements:
            if ranNum == 1:
                espeak.synth("I don't know what you mean by that")
            if ranNum == 2:
                espeak.synth("Your words are not in my library")
            if ranNum == 3:
                espeak.synth("No comment")

