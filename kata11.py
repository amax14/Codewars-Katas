def solution(args):

    s=''
    lt=[]
    ft=[]
    ct=[]
    m=0
    old_m=0
    itr = 0
    p=0

    ln = len(args)
   

    for m in args:
        dm = abs(m - old_m)
        old_m = m

        if dm > 1: 
            lt.append(0)
            itr = 1
        else:
            lt.append(itr)
            itr += 1
    
    for j,i in enumerate(lt):
        if i == 0:
            ft.append(str(args[j]))
        if i == 1:
            ft.append(str(args[j]))
        if i > 1:
            ft.append('')

    for j,i in enumerate(lt):
        if i == 1: p = j
        if i > 1:
            ft[p]='-'+str(args[j])

    for j,i in enumerate(lt):
        if i > 1:
            ft[j-2]+=ft[j-1]
            ft[j-1]=''                    
    
    for x in ft:
        if x!='':
            ct.append(x)

    s = ",".join(ct)
            
    return s

print(solution([-5]))
print(solution([1,2,3,4,5]))
print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])) #'-6,-3-1,3-5,7-11,14,15,17-20'
print(solution([-3,-2,-1,2,10,15,16,18,19,20])) #'-3--1,2,10,15,16,18-20'
print(solution([-63,-60,-58,-57,-54,-53,-50,-49,-46,-44--42,-39,-36,-34,-32,-30,-28,-25,-23,-20--16,-13--10,-7])) #'-63,-60,-58,-57,-54,-53,-50,-49,-46,-44--42,-39,-36,-34,-32,-30,-28,-25,-23,-20--16,-13--10,-7,-6'
