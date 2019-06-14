
class Bank



    '''
    sanitize function
    this function checks that the input value is a number and less than 10^9
    otherwise it returns False
    '''
    def sanitize(val):
        float(val)
        try:
            val = float(val)
            if val < 10**9:
                return True
            print('Invalid Input1')
            return False
        except ValueError:
            print(ValueError)
            print('Invalid Input2')
            return False

    '''
    balance function
    '''
    def balance(balance):
        print(f"balance: {balance}")
        pass


    '''
    Withdraw function
    this function updates the balance with a new value
    '''
    def withdraw():
        amount = input("Enter amout to withdraw\n\namount: ")

        #prevent code injection
        if sanitize(amount):
            amount = float(amount)
            if amount >= 0:
                bal = bal - amount
                balance(bal)
                return
            print ("Invalid Input3")
            return

        


    '''
    deposit function
    '''
    def deposit():
        print("balance")
        pass 
    def _exit():
        pass

    def enterCommand():
        commands = {

            'b' : balance,
            'w' : withdraw,
            'd' : deposit,
            'e' : _exit,
        }   
        
        command = input("Commands:\n(b)alance\n(d)eposit\n(w)ithdraw\n(e)xit\n\ncommand: ")
        if len(command) > 1:
            print("Invalid Input")
            return;
        print('im here weird')
        try:
            commands[command](bal)#(name="joe")#pass any key value to call the method
        except:
            print("Invalid Input4")




    bal = 10.0
    withdraw(bal)
    balance(bal)

    '''while True:
        print('q')
        enterCommand()
    '''