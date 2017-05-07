# -*- coding: utf-8 -*-
# --author-- = Urska Rifelj


print ""
print "Hello there...welcome to vehicle manager. Select letter respectively. \n \n " \
      "For list of vehicles = a \n For correction of km = b \n For correction of registration " \
      "date = c \n To add vehicle = d \n To remove vehicle = e \n To exit = f"

user_selection = raw_input("Enter valid letter: ")


class Vehicle (object):

    def __init__(self, brand, model, km, reg_date):
        self.brand = brand
        self.model = model
        self.km = km
        self.reg_date = reg_date

    def adjust_number_of_km(self):
        self.km = raw_input("Enter new value of km: ")

    def adjust_reg_date(self):
        self.reg_date = raw_input("Enter new date of registration: ")


vehicle1 = Vehicle("Volvo", "d234", 124556, "14.3.2007")
vehicle2 = Vehicle("Clio", "1j4", 128765456, "27.5.2000")
vehicle3 = Vehicle("Mazda", "24g", 9876, "1.2.2017")
vehicle4 = Vehicle("Audi", "dkd4", 7596, "14.9.2012")
vehicle5 = Vehicle("Master", "jlc4", 98743, "14.7.2011")
vehicle6 = Vehicle("Citroen", "jgf74", 43567, "14.11.2005")

vehicle_list = [vehicle1, vehicle2, vehicle3, vehicle4, vehicle5, vehicle6]


while user_selection == "a" or user_selection == "b" or user_selection == "c" or user_selection == "d" or user_selection == "e" or user_selection == "f":
    if user_selection == "a":        # list of vehicles with all attributes
        for item in vehicle_list:
            print item.brand
            print item.model
            print item.km
            print item.reg_date

    elif user_selection == "b":      #Correction of KM
        for item in vehicle_list:
            user_input_km = raw_input("Would you like to correct number of km of %s? d/n" % item.brand)
            if user_input_km == "d":
                item.adjust_number_of_km()
                print "New number of km made by %s is" % item.brand, item.km, "."
            elif user_input_km == "n":
                print "Number of km made by %s is still" % item.brand, item.km, "."
            else:
                print "Guess you did not enter valid response."

    elif user_selection == "c":      #Correction of registration date
        for item in vehicle_list:
            user_input_reg_date = raw_input("Would you like to correct registration date fo %s? d/n" % item.brand)
            if user_input_reg_date == "d":
                item.adjust_reg_date()
                print "New date of registration of %s is " % item.brand, item.reg_date, "."
            elif user_input_reg_date == "n":
                print "Registration date of %s is still" % item.brand, item.reg_date
            else:
                print "Guess you did not enter valid response."

    elif user_selection == "d":      #To add another vehicle
        while user_selection == "d":
            user_vehicle_brand = raw_input("please enter brand name")
            user_vehicle_model = raw_input("Please enter model")
            user_vehicle_km = raw_input("Please enter number of km")
            user_vehicle_reg_date = raw_input("Please enter registration date.")

            vehicle_n = Vehicle(user_vehicle_brand, user_vehicle_model, user_vehicle_km, user_vehicle_reg_date)
            vehicle_list.append(vehicle_n)
            print "You added", vehicle_n.brand, vehicle_n.model, "on a list."
            user_selection = raw_input("Would you like to add another vehicle in a list? d/n")


    elif user_selection == "e":         #To remove vehicle
        user_del_item = raw_input("which item would you like to remove from list? Enter valid branch name ")
        for item in vehicle_list:
            if item.brand == user_del_item:
                vehicle_list.remove(item)

    elif user_selection == "f":
        print "Bye, Bye"
        break

    print ""
    print "Select letter respectively. \n \n " \
          "For list of vehicles = a \n For correction of km = b \n For correction of registration " \
          "date = c \n To add vehicle = d \n To remove vehicle = e \n To exit = f"

    user_selection = raw_input("Enter valid leter: ")




