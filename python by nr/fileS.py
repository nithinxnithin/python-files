# tppes of files:
#  types of daata files:
# test files      
# binaray  files                     

#  writing  data to a file:
f=open("data.txt","w")
f.write("wello,python!\n")
f.close()

# wwritelines:  write a list of string to the file

f=open("data.txt","w")
f.writelines(["line1\n","line2\n","line3\n"])
f.close()


# readd:   

f=open("data.txt","r")
print(f.read())
print(f.read(5))
f.close()

 
#  readliness:
f=open("data.txt","r")
print(f.readline())
print(f.readline())
f.close()

f=open("data.txt","r")
lines=f.readlines
print(lines)
f.close()


# ramdom acess to file operations:

# example:
f=open("data.txt","r")
print(f.read(5))   #reads furst 5charectetrsss 
print("pointer at:",f.tell())
f.seek(0)
print(f.read(5))
f.close()