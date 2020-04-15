# api-design-kentpei
***
My weather.py contains the API from third party and it has two function.
First one si getinfo1, which you can input coordinates and get weather infomation.
Second one is getinfo2, which you can input city and get weather infomation.
***
weatherAPI.py is the main file, first it has getdata() to save data of airport names and coordinates in dictionary from csv file.
Then it has two function, first is search_city which imports getinfo2 from weather.py , so input city name can get you weather information
In addition, search_airport which imports getinfo1 from weather.py and you can input airport name and then you get coordinates from dic which help you get weather information.
***
Last, we have a file name test_weatherAPI test your main file. If your input is wrong or invalid , it returns 
"Input Error".
