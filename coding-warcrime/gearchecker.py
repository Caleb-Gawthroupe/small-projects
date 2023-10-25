#Coding warcrime one liner for a program my high school comp sci teacher made. Passed in an if statement as a list position and gathered all the input in one line.
print(["You need to wear a coat today","Skip the coat today"][((float(input("What is the temperature in fahrenheit? "))-32)/1.8 > 10)]+[" and pack the umbrella"," and don't worry about the umbrella"][float(input("What is the chance of rain? "))<29])
#My teachers "inificient" program was:
def celsius(f):
    return (f-32)/1.8

def gearchecker(f,rain):
    temp = celsius(f)
    message = ""
    
    if f < 10:
        message+="You need to wear a coat today"
    else:
        message+="Skip the coat today"
    
    if rain > 29:
        message+=" and pack the umbrella."
    else:
        message+=" and don't worry about the umbrella."
    return message
temp = float(input("What is the temp in fahrenheit? "))
chance = float(input("What is the chance of rain? "))
print(gearchecker(temp, chance))
