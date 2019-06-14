balance = 0.0
run = True
history = []
bal = []

print (balance)

'''
sanitise input. regect if input cant be cast to float. limit input to 30 characters (no one has a quintillion + dollars no need to allow unreasonable values)
'''
while run == True:
    input_data = raw_input("What would you like to do\ncommand: ")

    if(input_data == "balance"):
        print(balance)
        history.append("balace")
        bal.append(balance)
    elif(input_data =="deposit"):
        input_data = input("Enter deposite amount\nDeposit: ")
        balance = balance + input_data
        print("Total balance is now {}".format(balance))
        history.append("deposit -> ${}".format(input_data))
        bal.append(balance)
    elif(input_data == "withdraw"):
        input_data = input("How much would you like to withdraw\nWithdraw: ")
        if (float(input_data) < balance ):
            balance = balance - input_data
            print("Total balance is now {}".format(balance))
            history.append("withdraw <- ${}".format(input_data))
            bal.append(balance)
        else:
            print("Failed")
    elif input_data == "exit":
        run = False
        break
    elif input_data == "history":
        for i in range(0,len(history)):
            print("Transaction iD: {}".format(i))
            print(history[i])
            print("balance: ${}".format(bal[i]))
            print("---------------------")
    else: 
        print("Invalid selection!")

def isNum(num):
    try:
        float(num)
        return True
    except:
        return False