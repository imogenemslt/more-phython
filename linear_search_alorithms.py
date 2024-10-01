# serches for 17 in the list a gives back the posiotin
Mylist = [85, 24, 63, 45, 17, 31, 96, 50]
key = 17
for i in range(len(Mylist)):
    if Mylist[i] == key:
        location = i
print("key found at: ",location)
#same as the first code but goes backwars to find the first 17 using -1 arguements
mylist = [85, 24, 63, 45, 17, 31, 96, 17]
key = 17
for i in range(len(mylist)-1,-1,-1):
    if mylist[i] == key:
        location = i
print("key is found at",location)
#makeing a serch but with while loop
mylist =[85, 24, 63, 45, 17, 31, 96, 50]
key = 17
counter = 0
# makes found equal to false
found = False
print(mylist)
#not "false" equals to true
while (not found) and counter != len(mylist):
    if mylist[counter] == key:
        #makes the true statement turn false when  found key and ends the loop
        found = True
        location = counter
        print(location)
       
    else:
        counter += 1

        
    
    
    
    