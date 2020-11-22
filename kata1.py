def count_bits(n):
    b = bin(n)
    nums = 0
    for bc in b:
        if bc == '1': nums+=1
    return nums

num = int(input('Input non-negative number: '))

if num >= 0: 
    print(count_bits(num))
else: 
    print("Negative number")

print(count_bits(0)) # 0
print(count_bits(4)) # 1
print(count_bits(7)) # 3
print(count_bits(9)) # 2
print(count_bits(10)) # 2
