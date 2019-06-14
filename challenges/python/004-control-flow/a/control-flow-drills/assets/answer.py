# Write your program her
#!/usr/bin/python

import sys 
#hello because the conditional is True

#false because the conditional is False

pet = True

print("I have a pet" if pet else "I don't have a pet")


arg1 = sys.argv[1]
print("Hi, my name is {}".format(arg1) if arg1 =="kwajo" else "That isn't my name!!!")

level_8 = "reception"
level_13 = "old coder room"
level_12 = "classroom"
location = "classroom"

if level_8 == location:
    print("im on level 8")
elif level_13 == location:
    print("im on level 13")
elif level_12 == location:
    print("im on level 12")
else:
    print("im not at 120 spencer street")


#if location != level 8,12 or 13

coffee = input("How many coffees do you drink a day?\nCoffees: ")

if coffee > 3:
    print ("AHHHHH so much caffeine")
    
elif coffee > 2:
    print("hmm it's getting a bit much")
    
elif coffee > 1:
    print("i need my coffee hit")
    
elif coffee > 0:
    print("i need my coffee hit")
    
elif coffee == 0:
    print("saving $$")
    
    


num = input("Enter a number: ")

print("it's even" if num % 2 == 0 else "it's odd")
