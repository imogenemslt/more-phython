# #def defines displaymenu as a function of thr print statements
# def displayMenu():
#     print ("\t**********************************")
#     print ("\t* Menu *")
#     print ("\t**********************************")
# def menuOpt(optNumber):
#     print ("\t**********************************")
# #sets the optnumber in the menu opt as the input
#     print ("\t*","Option", optNumber)
#     print ("\t**********************************")
# displayMenu()
# userOpt = int(input("Enter your option : "))
# #sents menuOpt as userOpt
# menuOpt(userOpt)
# 
# 
# #making calculatar
# def calculate():
#     Num1= int(input("enter in your first number: "))
#     Num2= int(input("enter second number: "))
#     symble = input("do you want to d, m, a or s: ")
#     if symble == "m":
#         print (Num1 * Num2)
#     elif symble == "d":
#         print (Num1 / Num2)
#     elif symble == "a":
#         print (Num1 + Num2)
#     elif symble == "s":
#         print (Num1 - Num2)
#     else:
#         print("not a symble")
# print()
# calculate()

#emails
def validateEmail(emailAddressIn):
    if (emailAddressIn.count("@") == 1 and emailAddressIn.count(".") >= 1 and len(emailAddress) >= 8):
        return True
    else:
        return False
    emailAddress = input("enter your email: ")
    if (validateEmail(emailAddress)):
        print ("email check is valid")
    else:
        print("email not valid")
print()
email= input("enter an email:")
validateEmail(email)

#code wasnt working

#function chalenge

def calculations():
    kmA = personA * 21.23 * 2 / 100
    kmA = round(kmA, 2)
    print(kmA)
    kmB = personB_D * 21.23 * 2/ 100 + personB_C
    kmB = round(kmB, 2)
    print(kmB)
    print(personC)


personA = int(input("A: how many km away dose personA live from the course? : "))
personB_D = int(input("B: how many km did personB drive to the station? : "))
personB_C = int(input("B: how muchdid the train and taxi cost personB? : "))
personC = int(input("C: how much did the taxi and bus cost personC? : "))
calculations()

if personA >= 32:
    print ("personA can claim for the jurney")
else:
    print("personA cant claim for the jurney")
if personB_D >= 32:
    print("personB can claim for the jurney")
else:
    print("personB cant claim for the jurney")
    
#task 8 pg 203
    

