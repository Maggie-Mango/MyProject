import mydata

#user_input 
#nadine:
#organize a function that is a factory for if statements
# organize a function that asks user info
#organize a function that drives the program (l)
#print user_input

q1 = (raw_input("what neighborhood are you in? "))
q2 = (raw_input("today is... "))

def neighborhood():
	list = []
	for data in mydata.restaurants:
		x = data['Neighborhood']
		y = data['Days'].split(',')
		result = data['Restaurant/bar name'], data['Time'], data['Website'], data['address'], data['extra']
		if q1 in data['Neighborhood'] or q1.lower() in data['Neighborhood'] or q1.upper() in data['Neighborhood']: 
			for i in y:
				if q2 in i or q2.lower() in i or q2.upper() in y:
					return result 
		else:
			print "not found"
			break
print neighborhood()

