import re

def create_phone_number(n):

    s=''

    for c in n:
        s += str(c)
        
    result = re.sub(r'(\d{3})(\d{3})(\d{4})', r'(\1) \2-\3', s)

    return result

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) #"(123) 456-7890"
print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) #"(111) 111-1111"
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) #"(123) 456-7890"
print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0])) #"(023) 056-0890"
print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) #"(000) 000-0000"







