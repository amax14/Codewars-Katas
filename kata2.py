# Dictionary representing the morse code chart 
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-', 'SOS':'...---...', '!':'-.-.--'} 

def decodeMorse(morse_code):
  
    citext = ''
    message = ''
    i = 0
    s = 0
    sf = 0 #space flag enable
    abc =''
    for code in morse_code: 
        if code == ' ':
            if i > 0 :
                i=0                
                abc=list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                message+=abc
            elif i == 0:
                abc=''
            s+=1
            if abc!='' and abc!='.': sf=1
            citext=''                
        else:
            if s > 2 and sf==1:
                message+=' '
                sf=0
            citext+=code
            abc=''
            i=1
            s=0

    if citext!='':
        message+=list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]   
                               
    return message



print(decodeMorse('.... . -.--   .--- ..- -.. .'))

print(decodeMorse('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '))
