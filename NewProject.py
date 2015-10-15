import mydata
#neighborhood = raw_input("what neighborhood are you in?")
#day = raw_input("what day is it?")  
def restaurants(neighborhood):   
  for data in mydata.restaurants:
    day = data['Days'].split(',')
    # print day, type(day)
    neighborhood = data['Neighborhood']
    #print type(neighborhood)
    result = data['Restaurant/bar name'], data['Time'], data['Website'], data['address'], data['extra']
    #print result, "this is result"
    if data['Neighborhood'] == "Alamo Square":
      print"we got the alamo square"
print restaurants('Castro')
#       print day, 'this is day'
#       for i in day:
#         if i == 'Sunday':
#           print i
#           print result
#           break 
#         else:
#           print 'no happy hours in alamo square on sundays'
#           break
# user_input = restaurants(raw_input("What neighborhood are you in? "), raw_input("what day is it? "))

#organize a function that is a factory for if statements
# organize a function that asks user info
#organize a function that drives the program (l)
#print user_input
    #     if i == 'Monday':
    #       print result
    #       break
    #     if i == 'Tuesday':
    #       print result 
    #       break
    #     if i == 'Wednesday':
    #       print result
    #       break
    #     if i == 'Thursday':
    #       print result
    #       break
    #     if i == 'Friday':
    #       print result 
    #       break
    #     if i == 'Saturday':
    #       print result
    #       break
    #     else:
    #       "not found"
    # elif data['Neighborhood'] == "Bernal Heights":
    #   for i in day:
    #     if 'Sunday' in i:
    #       print result 
    #       break
    #     elif 'Monday' in i:
    #       print result
    #       break
    #     elif i == 'Tuesday':
    #         print result
    #         break
        # elif 'Wednesday in i':
        #   break
        # print result
        # elif i == 'Thursday':
        #   break
        # print result
        # elif i == 'Friday':
        #   break
        # print result 
        # elif i == 'Saturday':
        #   break
        # print result
# print restaurants("Bernal Heights", "Sunday")
  # for data in mydata.restaurants:
  #   if data['Neighborhood'] == "Castro":
  #     for i in day:
  #       if i == 'Sunday':
  #         print result 
  #       if i == 'Monday':
  #         print result
  #       if i == 'Tuesday':
  #         print result 
  #       if i == 'Wednesday':
  #         print result
  #       if i == 'Thursday':
  #         print result
  #       if i == 'Friday':
  #         print result 
  #       if i == 'Saturday':
  #         print result
  # for data in mydata.restaurants:
  #   if data['Neighborhood'] == "Cole Valley":
  #     for i in day:
  #       if i == 'Sunday':
  #         print result 
  #       if i == 'Monday':
  #         print result
  #       if i == 'Tuesday':
  #         print result 
  #       if i == 'Wednesday':
  #         print result
  #       if i == 'Thursday':
  #         print result
  #       if i == 'Friday':
  #         print result 
  #       if i == 'Saturday':
  #         print result  
  # for data in mydata.restaurants:
  #   if data['Neighborhood'] == "Cow Hollow":
  #     for i in day:
  #       if i == 'Sunday':
  #         print result 
  #       if i == 'Monday':
  #         print result
  #       if i == 'Tuesday':
  #         print result 
  #       if i == 'Wednesday':
  #         print result
  #       if i == 'Thursday':
  #         print result
  #       if i == 'Friday':
  #         print result 
  #       if i == 'Saturday':
  #         print result
  # for data in mydata.restaurants:
  #   if data['Neighborhood'] == "Duboce Triangle":
  #     for i in day:
  #       if i == 'Sunday':
  #         print result 
  #       if i == 'Monday':
  #         print result
  #       if i == 'Tuesday':
  #         print result 
  #       if i == 'Wednesday':
  #         print result
  #       if i == 'Thursday':
  #         print result
  #       if i == 'Friday':
  #         print result 
  #       if i == 'Saturday':
  #         print result    
  # for data in mydata.restaurants:
  #   if data['Neighborhood'] == "Embarcadero":
  #     for i in day:
  #       if i == 'Sunday':
  #         print result 
  #       if i == 'Monday':
  #         print result
  #       if i == 'Tuesday':
  #         print result 
  #       if i == 'Wednesday':
  #         print result
  #       if i == 'Thursday':
  #         print result
  #       if i == 'Friday':
  #         print result 
  #       if i == 'Saturday':
  #         print result
  # for data in mydata.restaurants:
  #   if data['Neighborhood'] == "Financial District":
  #     for i in day:
  #       if i == 'Sunday':
  #         print result 
  #       if i == 'Monday':
  #         print result
  #       if i == 'Tuesday':
  #         print result 
  #       if i == 'Wednesday':
  #         print result
  #       if i == 'Thursday':
  #         print result
  #       if i == 'Friday':
  #         print result 
  #       if i == 'Saturday':
  #         print result
  # for data in mydata.restaurants:
  #   if data['Neighborhood'] == "Haight":
  #     for i in day:
  #       if i == 'Sunday':
  #         print result 
  #       if i == 'Monday':
  #         print result
  #       if i == 'Tuesday':
  #         print result 
  #       if i == 'Wednesday':
  #         print result
  #       if i == 'Thursday':
  #         print result
  #       if i == 'Friday':
  #         print result 
  #       if i == 'Saturday':
  #         print result
  # for data in mydata.restaurants:
  #   if data['Neighborhood'] == "Hayes Valley":
  #     for i in day:
  #       if i == 'Sunday':
  #         print result 
  #       if i == 'Monday':
  #         print result
  #       if i == 'Tuesday':
  #         print result 
  #       if i == 'Wednesday':
  #         print result
  #       if i == 'Thursday':
  #         print result
  #       if i == 'Friday':
  #         print result 
  #       if i == 'Saturday':
  #         print result
  # for data in mydata.restaurants:
  #   if data['Neighborhood'] == "Inner Richmond":
  #     for i in day:
  #       if i == 'Sunday':
  #         print result 
  #       if i == 'Monday':
  #         print result
  #       if i == 'Tuesday':
  #         print result 
  #       if i == 'Wednesday':
  #         print result
  #       if i == 'Thursday':
  #         print result
  #       if i == 'Friday':
  #         print result 
  #       if i == 'Saturday':
  #         print result
  # for data in mydata.restaurants:
  #   if data['Neighborhood'] == "Marina":
  #     for i in day:
  #       if i == 'Sunday':
  #         print result 
  #       if i == 'Monday':
  #         print result
  #       if i == 'Tuesday':
  #         print result 
  #       if i == 'Wednesday':
  #         print result
  #       if i == 'Thursday':
  #         print result
  #       if i == 'Friday':
  #         print result 
  #       if i == 'Saturday':
  #         print result
  # for data in mydata.restaurants:
  #   if data['Neighborhood'] == "Mission":
  #     for i in day:
  #       if i == 'Sunday':
  #         print result 
  #       if i == 'Monday':
  #         print result
  #       if i == 'Tuesday':
  #         print result 
  #       if i == 'Wednesday':
  #         print result
  #       if i == 'Thursday':
  #         print result
  #       if i == 'Friday':
  #         print result 
  #       if i == 'Saturday':
  #         print result
  # for data in mydata.restaurants:
  #   if data['Neighborhood'] == "Nob Hill":
  #     for i in day:
  #       if i == 'Sunday':
  #         print result 
  #       if i == 'Monday':
  #         print result
  #       if i == 'Tuesday':
  #         print result 
  #       if i == 'Wednesday':
  #         print result
  #       if i == 'Thursday':
  #         print result
  #       if i == 'Friday':
  #         print result 
  #       if i == 'Saturday':
  #         print result
  # for data in mydata.restaurants:
  #   if data['Neighborhood'] == "NoPa":
  #     for i in day:
  #       if i == 'Sunday':
  #         print result 
  #       if i == 'Monday':
  #         print result
  #       if i == 'Tuesday':
  #         print result 
  #       if i == 'Wednesday':
  #         print result
  #       if i == 'Thursday':
  #         print result
  #       if i == 'Friday':
  #         print result 
  #       if i == 'Saturday':
  #         print result
# restaurants("Castro", "Friday")
#       elif data['Days'] == "Tuesday":
#         print data['Restaurant/bar name'], data['Time'], data['Website'], data['address'], data['extra']
#       elif data['Days'] == "Wednesday":
#         print data['Restaurant/bar name'], data['Time'], data['Website'], data['address'], data['extra']
#       elif data['Days'] == "Thursday":
#         print data['Restaurant/bar name'], data['Time'], data['Website'], data['address'], data['extra']
#       elif data['Days'] == "Friday":
#         print data['Restaurant/bar name'], data['Time'], data['Website'], data['address'], data['extra']
#       elif data['Days'] == "Saturday":
#         print data['Restaurant/bar name'], data['Time'], data['Website'], data['address'], data['extra']
#       elif data['Days'] == "Sunday":
#         print data['Restaurant/bar name'], data['Time'], data['Website'], data['address'], data['extra']
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

