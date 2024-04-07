import random
def pickup():
    a=random.randint(0,2)
    return a
def toss(n):
    face=random.choice(n)
    return face

l=[(0,0),(1,1),(0,1)]
#   0th   1st   2th coins
# 0 is head, 1 is tail.

sample_space=[] # includes coins which are picked and tossed and shows a head. 

for i in range(0,1000): # large no of tosses to apply 'weak law of large numbers'.
    coin_picked=pickup()
    if toss(l[coin_picked]) != 1:
        sample_space.append(coin_picked)

final=sample_space.count(2)/sample_space.count(0)
#probability of other side being tail given head is shown when picked random coin and tossed.
#Here it is probability of it being 2nd coin given a coin is randomly chosen and coin shows head.

print(final)