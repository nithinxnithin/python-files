#triangleeee 
a=int(input("enter  side of a triangle:"))
b=int(input("enter side of a triangle:"))
c=int(input("enter side of a triangle:"))
if a==b==c:
    print("equlateral")
elif a==b<c or a==b>c:
    print("isocless")
elif a>b>c or a<b<c or a>b<c or a<b>c :
    print("scalen")
