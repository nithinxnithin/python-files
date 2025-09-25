# an array is a data structure that stores multiple items of the same data type in a contiguous memory block_
# adv os array data types:
    # 1. fixed data type
    # 2.fast access  
    # 3.better for numerical date 
    # 4. sutrable for low level  operations 
    
    # create a integer array 
import array 
numbers=array.array('i',[1,2,3,4,5])
print(numbers)


# create a float array 
import array
floats=array.array('f',[1.1,2.2,3.3])
print(floats)



# imp notesss:
#  array is not designed for full string its only for single charecters  
#  for multiple string use list insted 

# operations on array :
import array 
nums=array.array('i',[10,20,30,40]) 
print(nums[0])
print(nums[2])
print(nums[-1])
print(nums[1])

# slicing array :
import array
nums=array.array('i',[10,20,30,40,50])
print(nums[1:4])
print(nums[::-1])


#adding elements::
import array 
nums=array.array('i',[1,2,3])
nums.append(4)
print(nums)    


# insert at specific index:
nums.insert(1,10)
print(nums)

#  remove at a specific indexxx 
nums.remove(10) 
print(nums)

#remove elements by index 
del nums[0]
print(nums)  





