num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

# Bitwise AND 
bitwise_and = num1 & num2

# Bitwise OR
bitwise_or = num1 | num2

# Bitwise XOR
bitwise_Xor = num1 ^ num2

# Bitwise NOT
bitwise_not_num1 = ~num1
bitwise_not_num2 = ~num2

# Bitwise left shift
left_shift= num1 << 1  

# Bitwise right shift 
right_shift = num2 >> 2

print(f"\n Bitwise AND of {num} & {num2} = {bitwise_and}")
print(f"\n Bitwise OR of {num1} | {num2} = {bitwise_or}")
print(f"\n Bitwise XOR of {num1} ^ {num2}= {bitwise_Xor}")
print(f"\n Bitwise NOT of {num1} = {bitwise_not_num1}")
print(f"\n Bitwise NOT of {num2} = {bitwise_not_num2}")
print(f"\n Bitwise left shift of {num1} << 1 = {left_shift}")
print(f"\n bitwise right shift of {num2} >> 2 = {right_shift}")


