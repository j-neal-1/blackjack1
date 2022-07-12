import random
import time

hand=[]

deck=['1c', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'jc', 'qc', 'kc', 
    '1d', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'jd', 'qd', 'kd', 
    '1h', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'jh', 'qh', 'kh',
    '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'js', 'qs', 'ks']

values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

playerhandvalue=0
playerhandvaluelist=[]
numindeck=51 
unimportantnum=2
while unimportantnum>0:
    numfordeck=random.randint(0, numindeck)
    hand.append(deck[numfordeck])
    deck.pop(numfordeck)
    playerhandvaluelist.append(values[numfordeck])
    values.pop(numfordeck)  
    unimportantnum=unimportantnum-1
    numindeck=numindeck-1

computerhandvalue=0
computerhand=[]
computerhandvaluelist=[]
unimportantnum=2
while unimportantnum>0:
    numfordeck=random.randint(0, numindeck)
    computerhand.append(deck[numfordeck])
    deck.pop(numfordeck)
    computerhandvaluelist.append(values[numfordeck])
    values.pop(numfordeck)  
    unimportantnum=unimportantnum-1
    numindeck=numindeck-1

for i in range(2):
    computerhandvalue=computerhandvalue+computerhandvaluelist[i]

for i in range(2):
    playerhandvalue=playerhandvalue+playerhandvaluelist[i]
    
print('your hand is', hand[0], hand[1])
print('the dealers hand is', computerhand[0])

playerhandvalueint=2
deal='yes'
while deal=='yes':
    next=input('hit or stand? ')
    if next=='hit':
        deal='yes'
        numfordeck=random.randint(0, numindeck)
        hand.append(deck[numfordeck])
        deck.pop(numfordeck)
        playerhandvaluelist.append(values[numfordeck])
        values.pop(numfordeck)
        playerhandvalue=playerhandvalue+playerhandvaluelist[playerhandvalueint]
        playerhandvalueint=playerhandvalueint+1
    
    if next=='stand':
        deal='no'
        break

    if playerhandvalue>21:
        print('you bust rip')
    print('your hand is', end=' '), print(*hand, sep=', ')

print('the dealer flips their other card. their hand is', computerhand[0], computerhand[1])
computerhandvalueint=2
while computerhandvalue<17:
    numfordeck=random.randint(0, numindeck)
    computerhand.append(deck[numfordeck])
    deck.pop(numfordeck)
    computerhandvaluelist.append(values[numfordeck])
    values.pop(numfordeck)
    computerhandvalue=computerhandvalue+computerhandvaluelist[computerhandvalueint]
    computerhandvalueint=computerhandvalueint+1
    time.sleep(1.5)
    print('the dealer takes another card. their hand is now', *computerhand)
if computerhandvalue>21 and playerhandvalue>21:
    print('you loose becuase blackjack is unfair rip'), exit()
if playerhandvalue>21:
    print('you loose because you are bad. you busted'), exit()
if computerhandvalue>21:
    print('you win good job. the dealer busted'), exit()
if computerhandvalue>playerhandvalue:
    print('you loose becuase the computer got a value of', computerhandvalue, 'and you got a value of', playerhandvalue), exit()
if playerhandvalue>computerhandvalue:
    print('you win becuase you got a value of', playerhandvalue, 'and the computer got a value of', computerhandvalue), exit()
else: print('f')