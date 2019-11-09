


for a in range(0,101):
    a=int(a)
    if (a % 3) == 0 and (a % 5) == 0:
        a='fizzbuzz'
        print(a)
    
    if (a % 3) == 0 and (a % 5) != 0:
       a='fizz'
       print(a)
      
    if (a % 5) == 0 and (a % 3) !=0:
        a='buzz'
        print(a)
    else:
        print(a)