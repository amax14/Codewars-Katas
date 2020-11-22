def expanded_form(num):

    s = ''
    digits = []
    n=0
    m=0
    old_m=0
    
    digits = list(x for x in list(map(int, str(num))))
    l=len(digits)-1

    while l >= 0:
        digits[n]*=(10**l)
        if digits[n]!=0:
            m=digits[n]
            if m!=0 and old_m!=0: s+=' + '
            s += str(digits[n])
            old_m=m
        n+=1
        l-=1 
     
    return s

print(expanded_form(12))    # '10 + 2'
print(expanded_form(42))    # '40 + 2'
print(expanded_form(70304)) # '70000 + 300 + 4'
print(expanded_form(9000000))
print(expanded_form(81780))
