def narcissistic( value ): 

    result=False
    sumn=0

    s=str(value)
    l=len(s)
    
    for c in s:
        sumn+=int(c)**l

    if sumn==value: result=True
    else: result=False

    return result


print(narcissistic(7))    # True, '7 is narcissistic'
print(narcissistic(371))  # True, '371 is narcissistic'
print(narcissistic(122))  # False, '122 is not narcissistic'
print(narcissistic(4887)) # False, '4887 is not narcissistic'
print(narcissistic(153))
