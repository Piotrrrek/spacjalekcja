'''
        ODWRACANIE n TABLIC k ELEMENTOWYCH
'''
# i=int(input())
# for n in range(i):
#    T=list(map(int,input().split()))
#    T.pop(0)
#    T=T[::-1]
#    #print(T)
#    s=''
#    for element in T:
#        s=s+str(element)+' '
#    print(s)
'''
        ODWRACANIE TABLICY
'''
# T=list(map(int,input().split()))
# T=T[::-1]
# s=''
# for element in T:
#    s=s+str(element)+' '
# print(s)
'''
        ROL     
'''
# i=int(input())
# for n in range(i):
#    T=list(map(int,input().split()))
#    k=T[1]
#    T.pop(0)
#    T.append(k)
#    T.pop(0)
#    #T=T[::-1]
#    #print(T)
#    s=''
#    for element in T:
#        s=s+str(element)+' '
#    print(s)
'''
        ROL (k)
'''
# i,k=map(int,input().split())
#
# T=list(map(int,input().split()))
# T1=T[:k]
# T2=T[k:]
# T3=T2+T1
# s=''
# for element in T3:
#    s=s+str(element)+' '
# print(s)
'''
        PODZIELNOŚĆ
'''
# t=int(input())
# x=1
#
# for n in range (t):
#    a,b,c=map(int,input().split())
#    for x in range (a):
#        if(x%b==0 and x%c!=0):
#            print(x)
#            x=x+1
'''
        KWADRATOWE
'''
# d=int(input())
# for n in range (d):
#    x=int(input())
#    x=x*x
#    print(x)
'''
        SREDNIA PREDKOSC
'''
# t = int(input())
# for n in range(t):
#     v1, v2 = map(int, input().split())
#     vsr = (2 * v1 * v2) / (v1 + v2)
#     print(int(vsr))
'''
        PARZYSTE NIEPARZYSTE
'''
# t=int(input())
# for n in range (t):
#     L=list(map(int,input().split()))
#     L.pop(0)
#     p=''
#     np=''
#     i=0
#     for element in L:
#         if(i%2==1):
#             p=p+str(element)+' '
#             i=i+1
#         else:
#             np=np+str(element)+' '
#             i=i+1
#     T=p+np
#     print(T)
'''
        POLOWA
'''
# t=int(input())
# for n in range(t):
#     s=input()
#     x=len(s)
#     x=x//2
#     print(s[:x:])
