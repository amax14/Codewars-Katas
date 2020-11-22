def order(sentence):

  number = ord('1')
  wi = 0
  wc = 0
  nstr=''
  wstr=[]

  nstr = [word for word in sentence.split()]
  lstr = len(nstr)

  while wi < lstr:
    for char in nstr[wi]:
        if char.isdecimal():
            nstr[wi], nstr[int(char)-1] = nstr[int(char)-1], nstr[wi]
            if wi==(int(char)-1):
                if wi>wc: wi-=1
                else:
                    wi+=1
                    wc+=1
            else:
                wi+=1 
                
  wstr.append(" ".join(nstr))   
    
  return wstr[0]

print(order("4of Fo1r pe6ople g3ood th5e the2"))
print(order("is2 Thi1s T4est 3a"))
print(order("2 1 4 3"))
print(order('s8ailor sh2all 3we d4o w5ith wha1t dru7nken a6'))
print(order('4 1 3 2 5 6 7 8 9'))
print(order("i1t 7would old5 h2igh ne6w be4 3eye"))
print(order('1make th2ere 4early ma5n numb3er'))
print(order('lea1ve last2 mak4e with3 lon5g t6hat good9 w8ant 7go'))

