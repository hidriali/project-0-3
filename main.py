#this program is named CraFinder for a company named AutoCountry.
#the program enables users to navigate through the menu options.

def CarFinder():


  print("AutoCountry")

 #recall the fuction  
CarFinder()

# display the list of cars 

AllowedVehiclesList= [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]


#start your loop 
while True:
   print()
   print("*******************************")

   print("AutoCountry Vehicle Finder v0.1")
   print("*******************************")
# declare/assign your variables choice-num1, choice-num2, choice-num3.
   choice_num1=("1. PRINT all Authorized Vehicles") 

   choice_num2=("2. SEARCH for Authorized Vehicle")
  
   choice_num3=("3. add authorized vehicle")

   choice_num4=("4. Exit")


  #allow the user to choose/inter a number from the menue after the menu loads. 
#use the backslash n to create a new line for each item in the menue.
   user_input=input("Please Enter the  following number below from the following menu:"+ "\n" + choice_num1 + "\n" + choice_num2 + "\n" + choice_num3 + "\n" + choice_num4 + "\n")
   
   
  #declare the variable nameVehich and enable the user to input the name of the vehicle.
   if user_input=="1":
     #I used the *, "\n" to print element in new lines. 
     
      print(*AllowedVehiclesList, sep = "\n")

# start your if statement to direct the user to the correct path after the user chooses a number from the menu.

#note must indent the codes below the while loop.


   if user_input == "3":
     nameVehich=input("Please Enter the full Vehicle name you would like to add:")
     AllowedVehiclesList.append(nameVehich)
     print()
     print("You have added  " +"" + (nameVehich) + "to an authorized vehicle")
     print()

   
      

#initilize continue statement to end the current iteration and start from the top of the program.

   continue