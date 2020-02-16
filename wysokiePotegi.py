from functools import lru_cache
a,n,d=map(int,input().split())

@lru_cache()
def pot_rek(a,n,d):
    if n==0:
        return 1%d
    elif n%2!=0:
        return (a*pot_rek(a,n-1,d))%d
    else:
        p=pot_rek(a, n // 2, d)
        return (p*p)%d
print(pot_rek(a,n,d))