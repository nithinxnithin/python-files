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