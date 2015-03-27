def imgLookup(searchTerm):
    import os
    import sys
    import time
    from urllib import FancyURLopener
    import urllib2
    import simplejson
    import cv2
    import numpy as np
    import urllib

    searchTerm = searchTerm.replace(' ','%20')

    class MyOpener(FancyURLopener): 
        version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
    myopener = MyOpener()

    for i in range(0,1):
        url = ('https://ajax.googleapis.com/ajax/services/search/images?' + 'v=1.0&q='+searchTerm+'&start='+str(i*1)+'&userip=MyIP')
        request = urllib2.Request(url, None, {'Referer': 'testing'})
        response = urllib2.urlopen(request)

        results = simplejson.load(response)
        data = results['responseData']
        dataInfo = data['results']

        for i in dataInfo:
            req = urllib.urlopen(i['unescapedUrl'])
            arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
            img = cv2.imdecode(arr,-1)
            r = 200.0 / img.shape[1]
            dim = (200, int(img.shape[0] * r))
     
            resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            cv2.imshow('Picture',resized)
            if cv2.waitKey() & 0xff == 27:
                quit()

        time.sleep(2)
