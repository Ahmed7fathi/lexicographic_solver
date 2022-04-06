import random
from time import sleep

word = input("Enter a word: ")
p = [word]


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




while len(p) < f:
    r = ''.join([random.choice(word) for i in range(len(word))])
    if r not in p:
        print("[+] Found : [{}]".format(r))
        p.append(r)

p.sort()
print(p)
