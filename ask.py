def ask():
    while True:
        try:
            result = int(input("enter a number"))
        except:
            print("enter a valid input")
        else:
            result = result ** 2
            print("thank you.... your number square is {}".format(result))       
ask()
