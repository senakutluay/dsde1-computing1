import math

def errors(length, gravity):


    a= isinstance(length, int)
    b= isinstance(gravity, int)
    if a == False:
        return Type Error
    elif b== False:
        return Type Error
    elif a == True and b== True and a<=0:
        return Value Error
    elif a == True and b== True and b<=0:
        return Value Error
def formula(x,y):
    return 2 * math.pi * math.sqrt(x/y)
def period(length, gravity):
    return formula(length, gravity)

    