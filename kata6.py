def move_zeros(array):
    arr=[]
    nz=0
    is_type = lambda x: type(x)

    for elem in array:
        if elem !=0:
            arr.append(elem)
        else:
            if is_type(elem)==bool:
                arr.append(elem)
            else: nz+=1               
    while nz>0:
         arr.append(0)
         nz-=1
         

    return arr

# returns[False,1,1,2,1,3,"a",0,0]    
print(move_zeros([False,1,0,1,2,0,1,3,"a"]))


print(move_zeros([1,2,0,1,0,1,0,3,0,1]))
print(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))
print(move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]))
print(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]))
print(move_zeros([0,1,None,2,False,1,0]))
print(move_zeros(["a","b"]))
print(move_zeros(["a"]))
print(move_zeros([0,0]))
print(move_zeros([0]))
print(move_zeros([False]))
print(move_zeros([]))

