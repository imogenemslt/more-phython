# #task 1
# #age is the varible and when int n need for print
# age = int(input("enter your age: "))
# score = int(input("enter your test score: "))
# if age >= 17:
#     if score >= 80:
#         #prints good if they are 17 or above and get abovw 80
#         print ("good!!")
#     else:
#         #prints try harder if they are over 17 and get ess then 80
#         print ("please try harder")
# else:
#     #prints excilent if they are under 17 and get above 80
#     print("excilent")

# #task 5
# email= (input("enter your email it must contain a @ and a . and be 8 or more carictors to be valid:"))
# target="@"
# #see page 22
# if (email.__contains__(target)) :
#     if (email.__contains__(".")):
#         if len(email) >= 8:
#             print("valid email proceed")
#         else:
#             print("invalid try again")
# else:
#     print("invalid try again")

#task 7
#makes the person add in lengh of sticks
stickA = int(input("enter in the smaller stick lengh and round up to neasrist cm"))
stickB = int(input("enter in the middle size stick rounding up to the cm"))
stickC = int(input("enter in the biggest stick rounding up to the cm"))
#makes sure stickC is the hypotenuse of the triangle
if stickA > stickB:
    print("invalid size")
    if stickB > stickC:
        print("invalid size")
        if stickC < stickB:
            print("invalid size")
        else:
            print("size is ok")
    else:
        print("size is ok")
else:
    print("size is ok")
#dose the calculations of the sizes to see if its right angle or not
if stickA**2 + stickB**2 == stickC**2:
    print("the sticks do make a right angle")
else:
    print("the sticks dont make a right angle")
           