while True:
    user_input=input("enter 'exit' to stop:")
    if user_input =='exit':
        print("logged in")
        break
    else:
        print("try again")
        
        
        
###continuee
#example:
for number in range(1,6):
    if number==3:
        print("skipping number 3")
        continue 
    print("number",number)
    
    
    for number in range(1,30):
        if number%3==0:
            print("skipping multiples of 3")
            continue
        print("number",number)
        
        
        
        for number in range(1,-10):
            if number==-number:
                print("skipping negative number")
                continue
            print("number", number)