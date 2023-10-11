# side0 = int(input("Choose first side "))
# side1 = int(input("Choose second side "))
# area0 = side0*side1
# print("The area of rectangle is " , area0)


# weight = int(input("Type your weight "))
# height = float(input("Type your height in meters "))
# IBM = weight/height**2
# if IBM < 18.5 :
#     print("You are thin - ", IBM)
# if IBM >= 18.5 and IBM < 25 :
#     print("You have normal IBM - ", IBM)
# if IBM >= 25 and IBM < 30 :
#     print("You a bit overweight - ", IBM)
# if IBM >= 30 and IBM < 35 :
#     print("You have first degree obesity - ", IBM)
# if IBM >=35 and IBM < 40 :
#     print("You have obesity class II - ", IBM)
# if IBM >= 40 :
#     print("You have third degree obesity - ", IBM)

# tempcelsius = int(input("Type temperature in celcius "))
# tempfarengheits = tempcelsius*1.8 + 32
# print(tempfarengheits, " it is your celsius in farengheits")

# income = int(input("Type how much many did you get in PLN "))
# if income <= 120000:
#     print(income*0.12 - 3600, "It is your tax")
# else :
#     print((income-120000)*0.32 + 10800, "It is your tax")
while True :
    num0 = int(input("Type your first number "))
    num1 = int(input("Type your second number"))
    action = input("Print which action you want to do ")
    if action == "+" :
        print("The sum of your numbers is ", num0 + num1 )
    if action == "-" :
        choose = int(input("From which number you want to substract(0 for first, 1 for second) "))
        if choose == 1:
            print(num1 - num0)
        else :
            print(num0 - num1)
    if action == "*" :
        print(num0*num1)
    if action == "/" :
        choose= int(input("Which number you want to divide(0 for first, 1 for second) "))
        if choose == 1 :
            print(num1/num0)
        else :
            print(num0/num1)
    repeatquestion = input("Do you want to rechoose?(Y/N) ")
    if repeatquestion == "N" :
        print("Thank you for using my calculator ")
        exit()
        
        
 