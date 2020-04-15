from datapackage import Package
from weather import *

def getdata():
    package = Package('https://datahub.io/core/airport-codes/datapackage.json')
    for resource in package.resources:
        if resource.descriptor['datahub']['type'] == 'derived/csv':
            content = resource.read()
    dic = {}
    print("\n")
    for data in content:
        if data[5] == "US":
            dic[data[2]] = data[-1]
    #print(dic["Total Rf Heliport"])
    return dic
def search_city(city):
    try:
        #print()
        return getinfo2(city)
    except:
        return "Input Error"
def search_airport(dic,airport):
    try:
        cor = dic[airport].split(",")
        info = getinfo1(float(cor[0]), float(cor[1]))
        #print()
        return airport + "  " + info
    except:
        return "Input Error"

'''
dic = getdata()
print(search_airport(dic,"General Edward Lawrence Logan International Airport"))
print(search_city("Newyork"))

print(search_airport(dic,"Total Rf Heliport"))
print(search_airport(dic,"Newark Liberty International Airport"))
print(search_airport(dic,"John F Kennedy International Airport"))
print(search_city("Boston"))
print(search_city("New York"))
'''
