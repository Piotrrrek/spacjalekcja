def polp(n):
    S = []
    y = 2
    result = 'NIE'
    while y<=n:
        while n % y == 0:
            S.append(y)
            n //= y
        y+=1

    if len(S)==2:
        result='TAK'
        return result
    else:
        result='NIE'
        return result

t=int(input())

for i in range (t):
    x=int(input())
    print(polp(x))