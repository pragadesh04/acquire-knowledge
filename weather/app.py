import requests, json
import geocoder

try:
    g = geocoder.ip('me')
    print(g)

    g_lat = g.latlng[0]
    g_lon = g.latlng[1]

    print(g.city, g_lat, g_lon)

except Exception as e:
    print(f"Error {e}")
# name = input()
# api_key = "XTSOjEYD5EjdSGzFRu1NhzOHmzJjSG6T"
# url = f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={name}"

# print(url)
# response = requests.get(url)

# data = response.json()
# location_key = data[0]["Key"]
# print(location_key)

# url_Condition = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey=XTSOjEYD5EjdSGzFRu1NhzOHmzJjSG6T"
# print(url_Condition)
# response = requests.get(url_Condition)

# data = response.json()

# print(data[0]["WeatherText"])
# print(data[0]["Temperature"]["Metric"]["Value"], end=' ')
# print(data[0]["Temperature"]["Metric"]["Unit"])