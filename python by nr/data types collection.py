# # collection data types are used to store multiple values in a single variable .
# # insted of creating seperate variables for each value ,we can group them togeather using collections 
# # why we can use collections ?

# # 1. store multiple data items together
# # 2.organise data for easy acess and maniplaction 
  
# #   types :
# #       list 
# #       tuple
# #       set
# #       dictonary  
# # list;
# # a collectons of ordered elements.lists are mutable(can be changed)

# # 1. ordered(maintains insetion order).
# # 2. mutable:can change,add, or remove elements.
# # 3. can contain duplicates.\
    
# # example:

fruits=['apple','banana','mango']
print(fruits)

# # adding an element:
fruits.append('orange')   
print(fruits)

# #remove an element:
fruits=['apple','banana','mango','grapes']
fruits.remove('banana')
print(fruits)

# #changing an clement :56
fruits[1]='grapes'
print(fruits)

# #acess an element from the list:
fruits=['apple','banana','mango','grapes','orange']


# #shirt list:
numbers =[5,2,9,1,7]
numbers.sort() 
print(numbers)

# #tuple;
# # collection of ordered elements that cannot be changed after creation .
# # Ordered 
# # immutable: once createdd not modified elements
# #    can  contains duplicates    'i
 # # example:
# dimensions=(10,20,30) 
# print(dimensions)
 
# # create a tuple of 5 colours and print itt 
colors=('red','black','orange','white','purple')
print(colors[0])
print(colors[3])
print(colors[-1])




# fruits=['apple','banana','mango']
if 'grapes'in fruits:
    print("grapes are in fruits")
else:
    print("grapes are not in the list ")
## tuple indexx 
fruits=('apple','banana','mango','grapes','orange')
print(fruits[0])
print(fruits[2])
print(fruits[-1])
print(fruits[-2])
# slicing :
# #     slicing helps exctract ,ultiple elememts at once using start  
# #step slicing every second eelement
fruits=['mango','banana', 'apple','orange']
print(fruits[::2])
 
#  #reverse tupleee
print(fruits[::-1]) 

# # count method ::

# # eexample:
numbers=(1,2,3,2,1,2)
count_2=numbers.count(2)
print(count_2) 
#index method :
# # find the first occurencess oof an element
# #EXAMPLEEEE :
fruits=('apple','banana','mango','apple')
index_apple=fruits.index('apple')
print(index_apple)
    
    
#     ##settt :
#     # collections of unordereed,uniqye elements 
    
# #adding elemenents :

unique_numbers={1,2,3,4,2,1}
unique_numbers.add(5)
print(unique_numbers)

#   #removing elements :
unique_numbers.remove(2)
print(unique_numbers)  


# #ddictonaryyy;;;;;;;

# # collections of key values pairs  , unorderedd but accessed by key :
# # store data as key values pair  

students={'name':'jhon',
          'age':20,
          'grade':'A',}
print(students)


# #access value by key

print(students['name'])

# # add new key value  
students['course']='CS'
print(students)  




# ###type conversionnnn ::::

# # list to tuplee:
my_list=[1,2,3,4] 
my_tuple=tuple(my_list)
print(my_tuple)
print(type(my_tuple))

# # set to  list::  
my_set={10,20,30}
my_list=list(my_set)
print(type(my_list))


# # 5.dictonary to list of keys:;:
student={'name':'john','age':20,'grade':'A'}
keys_list=list(student.keys)
print(keys_list)   

# 6. dictonary to list of values::

student={'name':'jhon','age':20,'grade':'A'}
values_list=list(student.values)
print(values_list)

#dictonary to list of  items::
student={'name':'john','age':20,}
item_list=list(student.item)
print(item_list)    



# loop break :
for number in range(1,10):
    if number==5:
        print("breaking the loop at number 5")
        break
    print("number:",number)
    
    
number=[1,2,3,4,5,6,7,8,9,]
if number%2==0:
    print("even")