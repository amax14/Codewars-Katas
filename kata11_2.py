def solution(seq):
    
    run = []
    res = []
    first, *rest = seq
    run.append(first)

    for n in rest+['end marker']:

        if n != run[-1] + 1:
            if len(run) > 2:
                res.append(f'{run[0]}-{run[-1]}')
            else:
                res += [str(r) for r in run]    #either one number, or two consecutive numbers
            run = [n]
        else:
            run.append(n)

        print(run)

    print(res)
    
    return ','.join(res)

print(solution([1,2,3,4,5]))
print(solution([-5]))
print(solution3([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])) #'-6,-3-1,3-5,7-11,14,15,17-20'
#print(solution([-3,-2,-1,2,10,15,16,18,19,20])) #'-3--1,2,10,15,16,18-20'
#print(solution([-63,-60,-58,-57,-54,-53,-50,-49,-46,-44--42,-39,-36,-34,-32,-30,-28,-25,-23,-20--16,-13--10,-7])) #'-63,-60,-58,-57,-54,-53,-50,-49,-46,-44--42,-39,-36,-34,-32,-30,-28,-25,-23,-20--16,-13--10,-7,-6'
