n=str(input())

def suma(n):
    N=[]
    sum=0
    for i in range (len(n)):
        N.append(int(n[i:i+1:]))
    for element in N:
        sum+=int(element)
    return sum

def sumaB(n):
    n=int(n)
    p=bin(n)
    p=p[2::]
    return suma(p)

print(suma(n),sumaB(n))