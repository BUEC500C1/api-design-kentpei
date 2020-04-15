from weatherAPI import *
def test():
    dic = getdata()
    assert search_airport(dic,"General Edward Lawrence Logan International Airport") != None
    assert search_airport(dic,"Total Rf Heliport") != None
    assert search_airport(dic, "Total Rf") == "Input Error"
    assert search_airport(dic,"Newark Liberty International Airport") != None
    assert search_airport(dic,"John F Kennedy International Airport") != None
    assert search_city("Boston") != None
    assert search_city("Newyork") == "Input Error"
    assert search_city("New York") != None
