type = input(str("What type? "))
first = float(input("First Number: "))
second = float(input("Second Number: "))
if type=="addition":
    
    sum = first + second
    print("sum: " + str(sum))
    
elif type=="subtraction":
    
     difference = first - second
     print("difference: " + str(difference))
     
elif type=="multiplication":

     product = first * second
     print("product: " + str(product))

elif type=="division":

     quotient = first / second
     print("quotient: " + str(quotient))
     remainder = first % second
     print("remainder: " + str(remainder))
     

else:
     
     print("your type is wrong")
     print("it must be either of these:")
     list = ["addition;", "subtraction;", "multiplication;", "division;"]
     for x in list:
          print(x)
     print("NOTE : ALL THE TYPES MUST BE IN LOWER CASES/SMALL LETTERS")