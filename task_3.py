import math as m

def simple_number(a):
    if a == 0 or a == 1:
        return False
    for i in range(2, int(m.sqrt(a))+1):
        if a % i == 0:
            return False
    return True

n = 1111111111111
d_max = 1

for k in range(n+1):    #перебираем делители n
    alpha = 0
    if simple_number(k) and (n % k == 0):
        while n % k == 0:
            n //= k
            alpha += 1
        print(k, alpha)
    if n == 1:
        break


