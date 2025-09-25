# functions :

# a funcctions is a block of code that is used to perform a specific taskk
# a function is a block of reusable code that performs a specific task_)



# why we use functionns :

# aviod repetitions of Code              

# syntax:
def fumction_name():
    print("hello,world")
    
    
    # example:
    def greet():
        print("welcome to python programming")
        greet
        
        
        # passing parameters
        def greet_user(name):
            print("hellow,",name)
            greet_user("hero")
            
            
            # function arguments types:
            # a) position argumentss
            # aarguments are passed in order  
            def add(a,b):
                print("sum is:",a+b)
                add(5,10)
                
                
                
# keyword arguments:
def introduce(name,age):
    print(F"my name is {name}and i am {age}years old")
    introduce(age=29,name="hero")
      
      
    #   default arguments:
    def greet(name="guest"):
        print("hellow,",name)
        greet()
        greet("ram")
        
        
# scope of variable:
# local varible
# global variable
x=100
def func():
    y=50
    print("inside function,x=",x)    
    print("inside function,y=",y)
    
func()
print("outside fumction,x=",x)
print(y)         #this will raise an error 
