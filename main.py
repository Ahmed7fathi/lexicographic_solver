import random
from time import sleep
word = 'abc'

def fact(n):
    if n <= 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fact(n-1)


f = fact(len(word))
print('possible choices ', f)
sleep(2)



p = []
p.append(word)

while len(p) < f:
    r = ''.join([random.choice(word) for i2 in range(3)])
    if r in p:
        pass
    else:
        print("[+] Found : [{}]".format(r))
        p.append(r)

p.sort()
print(p)