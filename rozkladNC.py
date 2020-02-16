n = int(input())
S = []
s = ''
i=2

while i<=n:
    while n % i == 0:
        S.append(i)
        n //= i
    i+=1
for element in S:
    s += str(element) + 'x'

print('=' + s[:len(s) - 1:])