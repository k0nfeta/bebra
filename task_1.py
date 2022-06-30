sum = 0
k = 0
while k <= 1000:
    if (k % 3 == 0) or (k % 5 == 0):
        sum += k
    k += 1
print(sum)
