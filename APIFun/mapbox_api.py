import requests

# https://account.mapbox.com/auth/signup/
# https://console.mapbox.com/
access_token = "YOUR ACCESS TOKEN"

# https://docs.mapbox.com/api/navigation/directions/
url = "https://api.mapbox.com/directions/v5/"
url += "mapbox/driving/"
url += "-117.4115166,47.6730239;-116.7583938,47.6641004" # GU to CDA Golf Resort
url += "?access_token=" + access_token
print(url)

response = requests.get(url)
# print(response.text)
json_obj = response.json()
# print(json_obj)
# TASK: parse the json object (dictionary) and print out
# the route distance in miles and duration in minutes
# get the first route object
route_obj = json_obj["routes"][0]
# print(route_obj)
# GS adding after class
distance_miles = route_obj["distance"] * 0.000621371
duration_mins = route_obj["duration"] / 60
print(f"route distance {distance_miles:.2f} miles and duration {duration_mins:.2f}")