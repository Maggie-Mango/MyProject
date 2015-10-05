import json
#Objects are in curly brackets
#Arrays are in brackets
#Git hub tutorial: http://readwrite.com/2013/10/02/github-for-beginners-part-2
#Tutorial: https://www.youtube.com/watch?v=xZKTtSw92nM
data = [
  {
    "Restaurant/bar name": "Ziryab",
    "Neighborhood": "Alamo Square",
    "Time": "5:00 - 7:00",
    "Days": "Monday, Tuesday, Wednesday, Thursday",
    "Website": "http://www.ziryabgrill.com",
    "address": "528 Divisadero St",
    "extra": "$4-5 select draft beers; $5 wines by the glass; $7 cocktails"
  }]
#print data
json_encoded = json.dumps(data)
json_decode = json.loads(json_encoded)
