import mydata
#neighborhood = raw_input("what neighborhood are you in?")
#day = raw_input("what day is it?)")

def restaurants(neighborhood, days):   
  for data in mydata.restaurants:
    days = data['Days'].split(',')
    print days 
print restaurants("Castro", "Saturday")
#     neighborhood = data['Neighborhood']
#     result = data['Restaurant/bar name'], data['Time'], data['Website'], data['address'], data['extra']
#     if data['Neighborhood'] == "Castro":
#       if days == "Friday":
#         print result
# restaurants("Castro", "Friday")
      # elif data['Days'] == "Tuesday":
      #   print data['Restaurant/bar name'], data['Time'], data['Website'], data['address'], data['extra']
      # elif data['Days'] == "Wednesday":
      #   print data['Restaurant/bar name'], data['Time'], data['Website'], data['address'], data['extra']
      # elif data['Days'] == "Thursday":
      #   print data['Restaurant/bar name'], data['Time'], data['Website'], data['address'], data['extra']
      # elif data['Days'] == "Friday":
      #   print data['Restaurant/bar name'], data['Time'], data['Website'], data['address'], data['extra']
      # elif data['Days'] == "Saturday":
      #   print data['Restaurant/bar name'], data['Time'], data['Website'], data['address'], data['extra']
      # elif data['Days'] == "Sunday":
      #   print data['Restaurant/bar name'], data['Time'], data['Website'], data['address'], data['extra']
#       else:
#          print "sorry no match your search results :("
# print restaurants("Castro", "Saturday")
    # if data['Neighborhood'] == "Alamo Square":
    #   if :
    # if data['Neighborhood'] == "Bernal Heights":
    #   print
    # if data['Neighborhood'] == "Cole Valley":
    #   print
    # if data['Neighborhood'] == "Cow Hollow":
    #   print
    # if data['Neighborhood'] == "Duboce Triangle":
    # if data['Neighborhood'] == "Embarcadero":
    # if data['Neighborhood'] == "Financial District":
    # if data['Neighborhood'] == "Haight":
    # if data['Neighborhood'] == "Hayes Valley":
    # if data['Neighborhood'] == "Inner Richmond":
    # if data['Neighborhood'] == "Marina":
    # if data['Neighborhood'] == "Mission":
    # if data['Neighborhood'] == "Nob Hill":
    # if data['Neighborhood'] == "NoPa":
    # if data['Neighborhood'] == "North Beach":
    # if data['Neighborhood'] == "SOMA":
    # if data['Neighborhood'] == "Sunset":
    # if data['Neighborhood'] == "Tenderloin":
    # if data['Neighborhood'] == "Union Square":
    # if data['Neighborhood'] == "Mission"

