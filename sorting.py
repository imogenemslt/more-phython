# # Insertion Sort
# #  
# # 1. Initialise an unsorted list
# # theList = [5, 7, 3, 6, 2]
# # 2. Initialise a marker
# # marker = 1
# #  
# # 3. Traverse through all list items
# # while (marker < len(theList)):
# #     # 4. Insert the selected item to its correct position
# #     j = marker
# #     while (theList[j] < theList[j-1] and j>0):
# #         tmp = theList[j]
# #         theList[j] = theList[j-1]
# #         theList[j-1] = tmp
# #         j = j-1
# #         
# #     # 6. Advance the marker to the right by 1 position
# #     marker = marker+1
# # print(theList)

 # Simple (Selection) Sort v1
 
# 1. Initialise an unsorted list
# aList = [9, 6, 10, 4, 8, 5, 7]
# # 2. Initialise a marker
# marker = 0 
#  
# # 3. Traverse through all list items
# while marker < len(aList):
#     # 4. Find the minimum item to the right of the marker
#     index_of_min = marker
#     for j in range(marker+1, len(aList)): 
#         if aList[index_of_min] > aList[j]: 
#             index_of_min = j
#     # 5. Exchange the smallest item with the item at the marker
#     temp = aList[marker] # save the item at the marker
#     aList[marker] = aList[index_of_min] # copy 1
#     aList[index_of_min] = temp # copy 2
#     
#     # 6. Advance the marker to the right by 1 position
#     marker = marker+1
#  
# # 7. Stop
# print(aList)

# #sets list
# myList = [85,24,63,45,17,31,96,50]
# #finds out how long the lsit is and makes a loop
# for i in range(1, len(myList)):
#     #prints list after every loop
#   print(myList)
#   #finds the 1 index in the list
#   itemInsert = myList[i]
#   #makes the index called posiotion 
#   position = i
#   #compares the index 1 to index 0 to determin wether then switch 
#   while position > 0 and myList[position-1] > itemInsert:
#       
#     myList[position] = myList[position-1]
#     position -=1
#     #sees if the positon is equal to the iteminsert
#   myList[position] = itemInsert
# #prints the final list after loop is completed 
# print(myList)

 
myList = [85, 24, 63, 45, 17, 31, 96,50]
# gets the length of the list but 2 index is used so -1 is required
for i in range(len(myList)-1):
    print(myList)
    for i in range(len(myList)-1):
        #compares the "0" index and the "0+1" index
        if myList[i] > myList[i + 1]:
            #sets tValue to index"0"
            tValue = myList[i]
            myList[i] = myList[i+1]
            myList[i+1] = tValue
print(myList)
  