def expanded_form(num):
     
    s = ''
    n=0
    m=0
    old_m=0

    st = str(num).split('.')

    ip = list(i for i in st[0])
    fp = list(i for i in st[1])

    digits=len(ip) 

    for j,i in enumerate(ip):
        n = int(i)*(10**((digits-1)-j))
        if int(i)!=0:
            m = n
            if m!=0 and old_m!=0: s+=' + '
            s += str(n)
            old_m = m          
    
    for j,i in enumerate(fp):
        n = int(i)
        if int(i) != 0:
            m = n
            if m!=0 and old_m!=0: s+=' + '
            s += str(n)
            s +='/'+str(10**(j+1))
            old_m = m
    return s

print(expanded_form(1.24))  #'1 + 2/10 + 4/100'
print(expanded_form(7.304)) #'7 + 3/10 + 4/1000'
print(expanded_form(0.04))  #'4/100'
print(expanded_form(693.23459))
