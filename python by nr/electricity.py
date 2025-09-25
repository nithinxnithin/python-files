#electricty     meter   
print("welcome to ninad bhai ka bathroom electricity ")
units =int(input("eneter tha units value "))
if units>=1 and units<=100:
    print("your total bill is: ",units*5)
elif units>=101 and units<=20:
    print("your total bill:",units*7)
elif units<200:
    print("your total bill is :",units*10)
