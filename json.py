import json
#Objects are in curly brackets
#Arrays are in brackets
#Git hub tutorial: http://readwrite.com/2013/10/02/github-for-beginners-part-2
#Tutorial: https://www.youtube.com/watch?v=xZKTtSw92nM
data = [
#use just one restaurant for now
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
#(isinstance of) Return true if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual)... 
#...subclass thereof. Also return true if classinfo is a type object (new-style class) and object is an object of that type or... 
#...of a (direct, indirect or virtual) subclass thereof. If object is not a class instance or an object of the given... 
#...type, the function always returns false. If classinfo is neither a class object nor a type object, it may be a tuple of 
#...class or type objects, or may recursively contain other such tuples (other sequence types are not accepted). 
#If classinfo is not a class, type, or tuple of classes, types, and such tuples, a TypeError exception is raised.
def u_out(input):
    if isinstance(input, dict):
        return {u_out(key):u_out(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [u_out(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input
hh_data = u_out(json_encoded)