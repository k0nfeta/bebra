f = 1 # первый
s = 1 # второй
sum = 0 # сумма
while s <= 4 * 10 ** 6:
    if s % 2 == 0:
        sum += s
    s = s + f
    f = s - f
print(sum)