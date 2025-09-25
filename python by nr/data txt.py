f = open("data.txt","w")
f.write("hello,python!\n")


f = open("data.txt","w")
f.writelines(["Line1\n","Line2\n","Line3\n"])
f.close


f = open("data.txt", "r")
print(f.read())
print(f.read(5))
f.close


f = open("data.txt", "r")
print(f.readline())
print(f.readline())
f.close


f = open("data.txt", "r")
Lines = f.readlines()
f.close


f = open("data.txt", "r")
print(f.read(5))
print("pointer at:",f.tell())
f.seek(0)
print(f.read(5))
f.close()  