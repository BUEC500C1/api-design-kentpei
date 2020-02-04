from weatherAPI import *
def test():
    dic = getdata()
    assert search_airport(dic,"General Edward Lawrence Logan International Airport") == 1
    assert search_airport(dic,"Total Rf Heliport") == 1
    assert search_airport(dic, "Total Rf") == "Input Error"
    assert search_airport(dic,"Newark Liberty International Airport") == 1
    assert search_airport(dic,"John F Kennedy International Airport") == 1
    assert search_city("Boston") == 1
    assert search_city("Newyork") == "Input Error"
    assert search_city("New York") == 1
