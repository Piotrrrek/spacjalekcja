def nwd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def nww(a,b):
    return a*b//nwd(a,b)

t=int(input())

for i in range (t):
    a,b=map(int,input().split())
    print(nwd(a,b))
    print(nww(a,b))