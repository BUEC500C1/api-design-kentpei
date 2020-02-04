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
        print(getinfo2(city))
        return 1
    except:
        return "Input Error"
def search_airport(dic,airport):
    try:
        cor = dic[airport].split(",")
        info = getinfo1(float(cor[0]), float(cor[1]))
        print(airport + "  " + info)
        return 1
    except:
        return "Input Error"
    '''
    for i in dic:
        cor = dic[i].split(",")
        info = getinfo(float(cor[0]), float(cor[1]))
        lst.append(str(i) + "  " + info)
    '''
'''
dic = getdata()
print(search_airport(dic,"General Edward Lawrence Logan International Airport"))
print(search_city("Newyork"))

search_airport(dic,"Total Rf Heliport")
search_airport(dic,"Newark Liberty International Airport")
search_airport(dic,"John F Kennedy International Airport")
search_city("Boston")
search_city("New York")
'''