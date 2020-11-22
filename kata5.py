def find_short(s):
    l=0
    sstr=[]
    sl = []

    for w in s.split():
        sstr.append(w)
    sl = sorted(sstr, key=len)
    l = len(sl[0])
    
    return l # l: shortest word length

def find_short1(s):
    s2=[]
    
    sl = [len(x) for x in s.split()]

    for x in s.split():
        s2.append(len(x))    
    
    print(sl)
    print(s2)
    return min(sl)


print(find_short1("bitcoin take over the world maybe who knows perhaps"))
print(find_short("turns out random test cases are easier than writing out basic ones"))
print(find_short("lets talk about javascript the best language"))
print(find_short("i want to travel the world writing code one day"))
print(find_short("Lets all go on holiday somewhere very cold"))
