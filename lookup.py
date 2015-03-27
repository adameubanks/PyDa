def lookup(input):
    import wikipedia
    from findpic import imgLookup
    from espeak import espeak
    if input.startswith('look up'):
        wikiLookUp = input[7:]
        print "Searched for: "+wikiLookUp
        espeak.synth("Searched for: "+wikiLookUp)
        print 'Results from wikipedia:'
        print wikipedia.summary(wikiLookUp)
        imgLookup(wikiLookUp)

    if input.startswith('who is '):
        wikiLookUp = input[7:]
        print "Searched for: "+wikiLookUp
        espeak.synth("Searched for: "+wikiLookUp)
        print wikipedia.summary(wikiLookUp)
        imgLookup(wikiLookUp)

    if input.startswith('who was '):
        wikiLookUp = input[8:]
        print "Searched for: "+wikiLookUp
        espeak.synth("Searched for: "+wikiLookUp)
        print wikipedia.summary(wikiLookUp)
        imgLookup(wikiLookUp)

    if input.startswith('what is '):
        print input[7:8]
        if input[8:10] == 'a ':
            wikiLookUp = input[10:]
            print "Searched for: "+wikiLookUp
            espeak.synth("Searched for: "+wikiLookUp)
            print wikipedia.summary(wikiLookUp)
            imgLookup(wikiLookUp)
        if input[8:11] == 'an ':
            wikiLookUp = input[11:]
            print "Searched for: "+wikiLookUp
            espeak.synth("Searched for: "+wikiLookUp)
            print wikipedia.summary(wikiLookUp)
        elif input[8:11] != 'an ' and input[8:10] != 'a ':
            wikiLookUp = input[8:]
            print "Searched for: "+wikiLookUp
            espeak.synth("Searched for: "+wikiLookUp)
            print wikipedia.summary(wikiLookUp)
            imgLookup(wikiLookUp)

    if input.startswith('where is '):
        wikiLookUp = input[9:]
        print "Searched for: "+wikiLookUp
        espeak.synth("Searched for: "+wikiLookUp)
        print wikipedia.summary(wikiLookUp)
        imgLookup(wikiLookUp)
    if input.startswith('how '):
        print "Searched for: "+input
        espeak.synth("Searched for: "+input)
        imgLookup(wikiLookUp)
