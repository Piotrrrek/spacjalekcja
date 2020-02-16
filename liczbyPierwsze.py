def pierw(x):
    if x == 1:
        return 'NIE'
    elif x == 2:
        return 'TAK'
    elif x % 2 == 0:
        return 'NIE'
    else:
        wynik = 'TAK'
        y = 3
        while y * y <= x:
            if x % y == 0:
                return 'NIE'
                break
            y = y + 2
        return wynik


n = int(input())

for i in range(n):
    x = int(input())
    print(pierw(x))