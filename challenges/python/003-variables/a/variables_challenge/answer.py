'''
def isNum(num):
    try:
	float(num)
	return True
    except:
        print("Not a number")
        return False



dSun = 149600000000.0

dist = input("Enter a number to recieve the % of distance from the sun in meters\nDistance:")
if isNum(dist):
    print("hi")
    pass
print ("The number you entered is {}% of the distance between the sun and earth in meters".format((dist/dSun)*100))

celcius = input("Enter the temperature in celcius to recieve the farenheight translation\nCelcius: ")

print ("The temperature in farenheight is {}".format((celcius*9/5)+32))

farenheight = input("Enter the temperature in farenheight to recieve the celcius translation\nFarenheight: ")

print ("The temperature in celcius is {}".format((farenheight-32)*5/9))


animals = input("How many animals do you have in your zoo?\nAnimals: ")
birds = input ("How many birds do you have in your zoo?\nBirds: ")
insects = input ("How many insects do you have in your zoo?\nInsects: ")

print ("The total number of legs in your zoo is {}".format(4*animals +2*birds +6*insects))

'''
fname = raw_input("What is your first name?\nName: ")
lname = raw_input("What is your last name?")
snum = raw_input("What is your street number?")
sname = raw_input("What is the name of your street?")
suburb = raw_input("What is the name of your suburb?")
city = raw_input("What is the name of your city?")


print ("Resident {} {} of {} {} lives in {}, {}".format(fname,lname,snum,sname,suburb,city))
