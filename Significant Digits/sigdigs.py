"""
Function to return the ammount of significant digits in a given number
"""

def sigdigs(num, ending):
    sig = 0
    num = str(num)
    trailers = 0
    
    if "." in num:
        decimal = True
    else:
        decimal = False
    if ending == True:
        decimal = True
    
    for char in num:
        if char == "0":
            if sig != 0:
                if decimal == True:
                    sig += 1
                else:
                    trailers += 1         
        else:
            if char != '.':
                sig+=1+trailers
                trailers = 0
                 
        if char == ".":
            decimal = True
        
        
            
    
    
    print(str(sig) + " Significant Digits")


while True:
    num = input()
    if num.lower() == "exit":
        exit()
    else:
        try:
            if num[-1] == ".":
                num = num[:-1]
                sigdigs(int(num), ending=True)
            else:
                sigdigs(num, ending=False)
        except:
            print("Error")
