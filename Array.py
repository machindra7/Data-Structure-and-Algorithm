
# # array model in python
# # spacecomplexity = "O(1)"
# import array
# my_array = array.array('i')    # timecomplexity = "O(1)"     # i is the typecode for integer in array model in python 
# print(my_array)                 # empty array

# my_array1 = array.array('i', [10, 20, 30, 40, 50])     # timecomplexity O(N)
# print(my_array1)

# # numpy model in python
# import numpy as np
# np_array = np.array([], dtype=int)     # timecomplexity = "O(1)"      # int is the data type for integer in numpy model in python 
# print(np_array)     # empty array

# np_array1 = np.array([10, 20, 30, 40, 50])       # timecomplexity O(N)
# print(np_array1)

# import array
# my_array = array.array('i', [1, 2, 3, 4]) 
# print(my_array)

# # insert at beginning        # timecomplexity = O(N)   # spacecomplexity = O(1)
# # my_array.insert(0, 6)  
# # print(my_array)

# # insert at middle 
# # my_array.insert(2, 5)
# # print(my_array) 

# # insert at end
# my_array.insert(4, 6)
# print(my_array)



# # Array traversal
# from array import *

# arr1 = array('i', [1, 2, 3, 4, 5])
# arr2 = array('i', [1, 2, 3, 4, 5, 6])

# def traverseArray(array):
#     for i in array:    # timecomplexity = O(N)    # spacecomplexity = O(1)
#         print(i) 

# traverseArray(arr1)


# # accessing an element in an array
# from array import *
# arr1 = array('i', [1, 2, 3, 4, 5])
# def accessElement(array, index):
#     if index >= len(array):
#         print("There is no element at this index")
#     else:
#         print(array[index])

# accessElement(arr1, 6)    # timecomplexity = O(1)    # spacecomplexity = O(1)



# # searching an element in an array
# import array
# my_array1 = array.array('i', [1, 2, 3, 4, 5])
# def searchElement(arr, target):
#     for i in range(len(arr)):               # timecomplexity = O(N)    # spacecomplexity = O(1)
#         if arr[i] == target:
#             return i
#     return -1
# print(searchElement(my_array1, 8))       # timecomplexity = O(N)    # spacecomplexity = O(1)



# delete an element from an array
from array import *
arr1 = array('i', [1, 2, 3, 4, 5])
arr1.remove(4)
print(arr1)    # timecomplexity = O(N)    # spacecomplexity = O(1)



