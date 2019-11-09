import math

def errors(length, gravity):


    a= isinstance(length, (int, float,complex))
    b= isinstance(gravity, (int, float, complex))
    
    
    if a == False:
        return 'TypeError'
    elif b== False:
        return 'TypeError'

def formula(x,y):
    return 2 * math.pi * math.sqrt(x/y)
def period(length, gravity):
    return formula(length, gravity)

    