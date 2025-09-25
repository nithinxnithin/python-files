# def mul(a,b):
#     print("mul is:",a*b)
#     mul(2,4)
    
    
    
# n1=int(input("enter a number"))
# n2=int(input("enter a number"))
# def mul_numbers(a,b):
#         return a*b
# result=mul_numbers(n1<n2)
# print(result)
    
    
    # q2:
    
# n=int(input("enter a number"))
# def is_even(num):
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
#         is_even(n) 
        
        # factoraial:
        # n1=int(input("enter number"))
        # def factorial(n):
        #     result=1
        #     for i in range(1, n+1):
        #         result*=i
        #         return result
        #     print(factorial(n1))
            
            
            
# n1=int(input("enter a number"))
# n2=int(input("enter a number"))
# n3=int(input("enter a number"))
# def largest_of_three(a,b,c):
#     if a>=b and a>=c:    
#         return a
#     elif b>=a and b>=c:    
#         return b
#     else:
#         return c    

# print(largest_of_three(n1,n2,n3))
                
            
#             # reverse stringgg:
# str=input("enter a string")
# def reverse_string(s):
#  return s[::-1]
# print(reverse_string(str))
            
# def count_vowels(word):
#     vowels="aeiouAEIOU"
#     count=0
#     for char in word:
#         if char in vowels:
#             count+=1
#             return count
#         print(count_vowels("programming"))
         
         
# ninadd=input("enter your nameee:")
# def count_vowels(ninad):
#     vowels="aeiouAEIOU"
#     count=0
#     for char in ninad:
#         if char in vowels:
#             count+=1
#             return count
#         print(count_vowels("programing"))
        
# python progrsmmingof higer order  functions :
# theses are the functions that either,
# take another functions as an arguemenets,or
# return   a   functions as a result
  
#   maps:
# example:
# def square(x):
#     return x*x
# numbers=[1,2,3,4,5]
# squared=list(map(square,numbers))
# print(squared)

# # filter:
# def is_even(x):
#     return x%2==0
# numbers=[1,2,3,4,5,6]
# even_numbers=list(filter(is_even,numbers))
# print(even_numbers)

# # c) reduce:
# # reudces a list to a single value by applying a binary function repeatedllllllllllllllllly:
# # example:
# # from funtools inport reducee   
# def add(x,y):
#     return x+y
# numbers=[1,2,3,4,5] 
# sum_numbers=(add,numbers)
# print(sum_numbers) 

# \
    
    # questions .22/09/2025:
    
 #1. substraction and multiplication 
val1=int(input("enter first number:" ))
val2=int(input("enter second number:"))
print("choose your option from the following:")
print("1.add")
print("2.substraction")
print("3.multiplication")
print("4.division ")

choose=float(input("enter your choice:"))

if choose == 1:
    print("result",val1+val2)
elif choose ==2:
    print("result",val1-val2)
elif choose ==3:
    print("result",val1*val2)
elif choose ==4:
    print(" result ",val1/val2)
    

i=int(input("enter a number"))
i2=int(input("enter second number"))
if i==i2:
    print("numbers are equal")
else:
    print("not equal")



a = 5
b = 3

a = a + b  
b = a - b  
a = a - b
