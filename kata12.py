def snail(snail_map):

    l_snail = []
    n = 0

    j_max = len(snail_map[0])
    i_max = len(snail_map)

    size = i_max * j_max
    j_max -= 1
    i_max -= 1
        
    j_min = 0
    i_min = 0

    i = i_min
    j = j_min

    while n < size:

        if j_min!=j_max:
            
            if i==i_min and j < j_max:
                l_snail.append(snail_map[i][j])
                j+=1
    
            if i < i_max and j==j_max:
                l_snail.append(snail_map[i][j])
                i+=1

        if i_min!=i_max:
            
            if i==i_max and j > j_min:
                l_snail.append(snail_map[i][j])
                j-=1
            
            if i > i_min and j==j_min:
                l_snail.append(snail_map[i][j])
                i-=1
                
        if i == i_max and j==j_max:
            l_snail.append(snail_map[i][j])

        if i==i_min and j==j_min:
            i_max-=1
            j_max-=1
            i_min+=1
            j_min+=1
            i=i_min
            j=j_min
           
        n+=1
    
    
    return l_snail



array = [[1,2,3,23],
         [4,5,6,24],
         [7,8,9,25],
         [7,8,9,25]]

expected = [1,2,3,6,9,8,7,4,5]

print(snail(array)) #expected


array = [[1,2,3],
         [8,9,4],
         [7,6,5]]

expected = [1,2,3,4,5,6,7,8,9]

print(snail(array))  #expected
