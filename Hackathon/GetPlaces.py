# import requests

import urllib, json 


def getPlaces(inquiryString, startLocation, radius): # pubs or what, latlng of user, radius, 
    # fix inquiry string
    # inquiryString = str(inquiryString).replace(" ", "%20")#+ "&inputtype=textquery"
    inputPart = "type=" + inquiryString+ "&"
    fieldsPart = "fields=formatted_address"+ "&"
    startLocation = "location="+ startLocation + "&"
    radius = "radius="+radius+ "&"# in meters
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?" + startLocation+ inputPart + fieldsPart +radius +"key=AIzaSyDXKLWHJQdqzVI1agSREbzr4AuoBKyUeuE"    

    print url
    # with urllib.request.urlopen(urlToRead) as url:
    #     data = json.loads(url.read().decode())
    #     print(data)
    response = urllib.urlopen(url)

    data = json.loads(response.read())

    print data


getPlaces("bar", "51.7520220,-1.2577260", "50")
