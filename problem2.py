max = 4000000
n1 = 1
n2 = 1
sum = 0
while (n2 <= max):
    if n2 % 2 == 0:
        sum += n2
    n1, n2 = n2, n1 + n2
print(sum)
