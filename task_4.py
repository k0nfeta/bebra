def length_number(n):
    k = 1
    while True:
        if (n // 10 == 0):
            return k
        n //= 10
        k += 1

def digit_number(n, k):
    return (n // 10 ** k) % 10

def polyndrom_test(n):
    for i in range(length_number(n) // 2):
        if digit_number(n, i) != digit_number(n, length_number(n) - i - 1):
            return False
    return True

max_p = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        if polyndrom_test(i*j) and i*j > max_p:
            max_p = i*j
print(max_p)


