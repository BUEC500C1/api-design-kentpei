import requests
import json

def getinfo1(x,y):
    url = "http://api.openweathermap.org/data/2.5/weather?" + "lat=" + str(y) + "&lon=" + str(x) + "&APPID=(your key's here)"
    content = requests.get(url).content
    new = content.decode("utf-8")
    content_json = json.loads(new)
    #print(new)
    #name = content_json["name"]
    temp , mintemp , maxtemp = content_json["main"]["temp"] , content_json["main"]["temp_min"] , content_json["main"]["temp_max"]
    weather = content_json["weather"][0]["main"]
    return ("weather:" + str(weather) + "  "  +  "temperatue:" + str(temp) + "  "  + "minimum temperature:" +
            str(mintemp) + "  "  + "maximum temperature:" + str(maxtemp))
def getinfo2(city):
    url = "http://api.openweathermap.org/data/2.5/weather?" + "q=" + city + "&APPID=9(your key's here)"
    content = requests.get(url).content
    new = content.decode("utf-8")
    content_json = json.loads(new)
    #print(new)
    #name = content_json["name"]
    temp , mintemp , maxtemp = content_json["main"]["temp"] , content_json["main"]["temp_min"] , content_json["main"]["temp_max"]
    weather = content_json["weather"][0]["main"]
    return ("name:" + city + "  " + "weather:" + str(weather) + "  "  +  "temperatue:" + str(temp) + "  "  + "minimum temperature:" + str(mintemp) + "  "  +
            "maximum temperature:" + str(maxtemp))
