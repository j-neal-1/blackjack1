import random

hand=[]
deck=['1c', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'jc', 'qc', 'kc', 
    '1d', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'jd', 'qd', 'kd', 
    '1h', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'jh', 'qh', 'kh',
    '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'js', 'qs', 'ks']
real1c='ace of clubs'; real2c='two of clubs'


numindeck=51
unimportantnum=2
while unimportantnum>0:

    numfordeck=random.randint(0, numindeck)

    print(numfordeck)

    hand.append(deck[numfordeck])
    deck.pop(numfordeck)

    print(hand)
    unimportantnum=unimportantnum-1
    numindeck=numindeck-1

print('your hand is', hand[0], hand[1])