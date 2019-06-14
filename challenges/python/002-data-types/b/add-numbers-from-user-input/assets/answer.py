def add_user_input():
    n1 = input("Enter number 1: ")
    if(isNum(n1) == False):
#        print("Please enter a number")
        return
    n2 = input("Enter number 2: ")
    if(isNum(n2) == False):
#        print("Please enter a number")
        return
#    print(f'Number 1: {n1} \nNumber 2: {n2}')
#    print(float(n1)+float(n2))
    return int(n1)+int(n2)
def isNum(num):
    try:
        float(num)
        return True
    except ValueError:
        return False 

#add_user_input()
