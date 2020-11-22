def persistence(n):
    
    i=0
    num = n

    while num > 9:
        snum=str(num)
        digit = list(snum)
        num=1
        for d in digit:
            num *= int(d)
        i+=1
    
    return i

print(persistence(39))
print(persistence(999))
print(persistence(4))
print(persistence(25))
