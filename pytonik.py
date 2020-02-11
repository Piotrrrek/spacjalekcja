# from functools import lru_cache
#
# F=[0,1]
# Fi=[0,1]
# Fr=[0,1]
#
# n=int(input())
#
# def fibo_iter(n):
#     if n<2:
#         return n
#     else:
#         a=0
#         b=1
#         for i in range(2, n+1):
#             c=a+b
#             a=b
#             b=c
#         return c
#
# @lru_cache() # domyślnie max - 128
# def fibo_rek(n):
#     if n<2:
#         return n
#     else:
#         return fibo_rek(n-2)+fibo_rek(n-1)
#
# for i in range (2, n+1):
#     F.append(F[i-2]+F[i-1])
#     Fi.append(fibo_iter(i))
#     Fr.append(fibo_rek(i))
#
# print(F[n])
# print(fibo_iter(n))
# print(fibo_rek(n))
# print(Fi)
# print(Fr)
# import time
#
# def pierw(n):
#     if n == 0 or n == 1:
#         return 'NIE'
#     elif n == 2:
#         return 'TAK'
#         # return wynik;
#     elif n % 2 == 0:
#         return 'NIE'
#         # return wynik;
#     else:
#         wynik = 'TAK'
#         i = 3
#         while i * i <= n:
#             if n % i == 0:
#                 wynik = 'NIE'
#                 break
#             i = i + 2
#         return wynik
#
# for i in range(100000):
#     #    n = int(input())
#     if (pierw(i) == 'TAK'):
#         print(i, pierw(i))
#         # time.sleep(0.3)
#
'''
        ALGORYTM EUKLIDESA
        # NWD(84,60) = 2 * 2 * 3 = 12
        # 84 | 2      60 | 2
        # 42 | 2      30 | 2
        # 21 | 3      15 | 3
        #  7 | 7       5 | 5
        #  1 |         1 |
         NWD(84,60) = NWD(84-60,60) = NWD (24,60) = NWD(24,60-24) = NWD(24,36) =
         = NWD(24,36-24) = NWD(24,12) = NWD(12,12) = 12

        |_______________|__________|___
                        \_________/
        0             a=60   |   b=84
                            b-a
                    -
                   | NWD(a, b-a) dla  b>a
        NWD(a,b)= |  NWD(a-b,b)  dla  a>b
                   |     a       dla  a=b
                    -
'''
#
# a, b = map(int, input().split())
#
#
# def nwdi(a, b):
#     while a != b:
#         # print('a=', a, 'b=', b)
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     return a
#
#
# def nwd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
#
# print(nwd(a,b))
# print(nwdi(a, b))
'''
        ARYTMETYKA MODULARNA
        234**567890    
        # WYSOKIE POTĘGI
'''
#
# a,n=map(int,input().split())
# w=1
# for i in range(n):
#     w=(w*a)%1000
# print(w)
#
# def pot_rek(a,n):
#     if n==0:
#         return 1
#     else:
#         return (a*pot_rek(a,n-1))%1000
#
# w=pot_rek(a,n)
# print(w)

'''               __________________________________________
                 |                                          |
                |  1 dla n=0                                |
          a^n=-|   a*a^(n-1) dla n nieparzystego, n>0       |
                |  a^(n/2)*a^(n/2) dla n parzystego, n>0    |
                 |__________________________________________|
'''
# from functools import lru_cache
# a,n,d=map(int,input().split())
#
# @lru_cache()
# def pot_rek(a,n,d):
#     if n==0:
#         return 1%d
#     elif n%2!=0:
#         return (a*pot_rek(a,n-1,d))%d
#     else:
#         p=pot_rek(a, n // 2, d)
#         return (p*p)%d
# print(pot_rek(a,n,d))

'''
        RESZTA Z DZIELENIA
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        |Działanie |a=20, b=6|a=20, b=-6|a=-20, b=6|a=-20, b=-6|
        |Reszta    |    2    |     2    |     4    |     4     |
        |a%b       |    2    |    -4    |     4    |    -2     |
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        a=k*b+r
        0<=r<|b|
        20=k*6+r
        20=3*6+2

'''
#
# d=int(input())
#
# for i in range (d):
#     a,b=map(int,input().split())
#     r=a%b
#     print(r)
#
'''
        OBLICZANIE PIERWIASTKA KWADRATOWEGO METODĄ Newtona-Raphsona
'''
#
#
# def pierwiastek(a, p):
#     x = a / 2
#     while -p > a / x - x or a / x - x > p:
#         y = a / x
#         x = (x + y) / 2
#         print(x)
#     return x
#
#
# def pieerwiastek(a):
#     x = a / 2
#     d = 0.00000001
#     while (x - a / x < -d) or (x - a / x > d):
#         x = (x + a / x) / 2
#     return x
#
#
# a,p=map(float, input().split())
# a = float(input())
# print(pieerwiastek(a))
# i=float(pierwiastek(a,p))
# print(i)
# print(i*i)
'''
        ROZKŁAD NA CZYNNIKI PIERWSZE
'''
# n = int(input())
# S = []
# s = ''
# i=2
#
# while i<=n:
#     while n % i == 0:
#         S.append(i)
#         n //= i
#     i+=1
# for element in S:
#     s += str(element) + 'x'
#
# print('=' + s[:len(s) - 1:])
'''
        SCHEMAT HORNERA
'''
# n=int(input())
# T=list(map(float, input().split()))
# x=float(input())
#
# T.reverse()
# w=T[n]
#
# for i in range(n-1,-1,-1):
#     w=w*x+T[i]
#
# print(w)
'''
        CAŁKOWANIE NUMERYCZNE
'''
# xp, xk = map(float, input().split())
#
#
# def f(x):
#     return x * x
#
#
# def pole_mp(xp, xk, n):
#     sz = (xk - xp) / n
#     P = 0
#     for i in range(n):
#         x0 = xp + i * sz
#         x1 = x0 + sz / 2
#         x2 = x0 + sz
#         y0 = f(x0)
#         y1 = f(x1)
#         y2 = f(x2)
#         P = P + sz * y1
#     return P
#
#
# def pole_mt(xp, xk, n):
#     sz = (xk - xp) / n
#     P = 0
#     for i in range(n):
#         x0 = xp + i * sz
#         x1 = x0 + sz / 2
#         x2 = x0 + sz
#         y0 = f(x0)
#         # y1 = f(x1)
#         y2 = f(x2)
#         P = P + (sz*(y0+y2)/2)
#     return P
#
# def pole_ms(xp,xk,n):
#     sz = (xk - xp) / n
#     P = 0
#     for i in range(n):
#         x0 = xp + i * sz
#         x1 = x0 + sz / 2
#         x2 = x0 + sz
#         y0 = f(x0)
#         y1 = f(x1)
#         y2 = f(x2)
#         P = P +(y0+4*y1+y2)*sz / 6
#     return P
#
#
# print(pole_mp(xp, xk, 100))
# print(pole_mt(xp, xk, 100))
# print(pole_ms(xp,xk,25))
'''
        CAŁKOWANIE NUMERYCZNE
'''
# xp=0
# xk=float(input())
#
# def f1(x):
#     return (-x*x)/50
#
# def f2(x):
#     return -(1+x*x/100-x/200)
#
# def pole1(xp,xk,n):
#     sz = (xk - xp) / n
#     P = 0
#     for i in range(n):
#         x0 = xp + i * sz
#         x1 = x0 + sz / 2
#         x2 = x0 + sz
#         y0 = f1(x0)
#         y1 = f1(x1)
#         y2 = f1(x2)
#         P = P +(y0+4*y1+y2)*sz / 6
#     return P
#
# def pole2(xp,xk,n):
#     sz = (xk - xp) / n
#     P = 0
#     for i in range(n):
#         x0 = xp + i * sz
#         x1 = x0 + sz / 2
#         x2 = x0 + sz
#         y0 = f2(x0)
#         y1 = f2(x1)
#         y2 = f2(x2)
#         P = P +(y0+4*y1+y2)*sz / 6
#     return P
#
# pole=pole1(xp,xk,10)+pole2(xp,xk,10)
# pole*=-1
# print(pole)
'''
        MIEJSCE ZEROWE FUNKCJI
'''
# a, b, c, d = map(float, input().split())
# xp, xk = map(float, input().split())
#
#
# def f(a, b, c, d, x):
#     return a * x * x * x + b * x * x + c * x + d
#
#
# def miejsce_zerowe(a, b, c, d, xp, xk):
#     xs = (xp + xk) / 2
#     if f(a, b, c, d, xs) == 0 or xk-xp<0.000000001:
#         return xs
#     elif f(a, b, c, d, xp) * f(a, b, c, d, xs) < 0:
#         return miejsce_zerowe(a, b, c, d, xp, xs)
#     else:
#         return miejsce_zerowe(a, b, c, d, xs, xk)
#
#
# print(miejsce_zerowe(a, b, c, d, xp, xk))
'''
        POLE WIELOKĄTA
'''
# n=int(input())
# X=[]
# Y=[]
# p=0

# for i in range (n):
#     x_temp,y_temp=map(float,input().split())
#     X.append(x_temp)
#     Y.append(y_temp)

# for i2 in range (n):
#     p=p+X[i-1]*Y[i]-X[i]*Y[i-1]

# if p<0:
#     p=-p

# p=p/2
# print(p)
'''
        WSPÓŁLINIOWOŚĆ PUNKTÓW
'''
# xA,yA=map(int,input().split())
# xB,yB=map(int,input().split())
# xC,yC=map(int,input().split())

# def w(x1,y1,x2,y2,x3,y3):
#     return x1*y2+x2*y3+x3*y1-x3*y2-x1*y3-x2*y1

# if w(xA,yA,xB,yB,xC,yC)==0:
#     print('TAK')
# else:
#     print('NIE')
'''
        NAJBLIŻSZY PUNKT
'''
# import math

# a,b,c=map(float,input().split())
# n=int(input())
# x_nb,y_nb=map(int,input().split())
# d_min=(abs(a*x_nb+b*y_nb+c))/math.sqrt((a*a)+(b*b))

# for i in range(n-1):
#     x,y=map(int,input().split())
#     d=(abs(a*x+b*y+c))/math.sqrt((a*a)+(b*b))
#     if d<d_min:
#         d_min=d
#         x_nb=x
#         y_nb=y

# print(x_nb, y_nb)
