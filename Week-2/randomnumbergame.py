

import random

print('what')
secretNumber=random.randint(1, 10)

for guessestaken in range(1,6):
    guess=int(input())

    if guess>secretNumber:
        print('too hiigghh')
    elif guess<secretNumber:
        print('too low')
    else:
        break
if secretNumber == guess:
    print('congrats')
else:
    print('nope it was' + secretNumber+ 'Try again')



