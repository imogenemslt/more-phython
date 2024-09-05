# 
# for i in range(4):
#     for j in range(5):
#         print(i,j)
# 
# #outer loop runs the inner loop runas as many times as the number in the braqkets
# for i in range(4):
#     #iner loop runs 5 times starting from 1 as many times as the outer loop says
#     for j in range(1, 6):
#         #end=" " makes it stay on one line
#         print(j, end=" ")
#         #makes the line go to the next line after the inner loop goes around
#     print()
# 
# #Nested loops are efficient because they use fewer lines of code.
# print("*****")
# print("*****")
# print("*****")
# print("*****")
# print("*****")
# 
# # write code to display 5 cols and 5 rows
# 
# #pg191
# 
# cols = 5
# for colIndex in range(cols):
#   print("*", end = "")
#   #end is used to stop adding a new line each time
# 
# #pg191
# 
# cols = 5
# rows = 4
# for rowIndex in range(rows):
#   for colIndex in range(cols):
#     print("*", end = "")
#   #this add a new line after each row iteration
#   print()
# 
# #pg192  
#   
# timesTable = 1
# for timesTable in range(1,11):
#   print(timesTable, ": Times Table")
#   for i in range(1,11):
#     ans = i * timesTable
#     #make all the equals line up nicely
#     if ans <= 90:
#       print (timesTable, "X", i, "\t\t=",ans)
#     else:
#       print (timesTable, "X", i, "\t=",ans)

#task 1
#(i) the inner loop is use to use less lines of code and makes it less time consuming
#(ii) the "print()" makes the loop go down a line before starting the outer loop again it makes it
#tidier
#(iii) the "*" will go across 50 times and will go down 10 times.
      
#task 3
  
cols = int(input("enter amount of colons wanted: "))
rows = int(input("enter the amount of rows wanted: "))
for i in range(rows):
    for j in range(cols):
        print("*", end = " ")
    print()