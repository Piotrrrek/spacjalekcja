n = int(input())
T = list(map(int, input().split()))
A=[]
B=[]

for i in range(n//2+2):
    A.append(0)
    B.append(0)

nieskonczonosc=10000000000

def scalaj(p,s,k):
    for i in range(p,s+1):
        A[i-p]=T[i]

def sortScal(p,k):
    if p<k:
        s=(p+k)//2
        sortScal(p,s)
        sortScal(s+1,k)
        scalaj(p,s,k)
