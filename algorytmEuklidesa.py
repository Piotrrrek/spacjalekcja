'''
        # NWD(84,60) = 2 * 2 * 3 = 12
        # 84 | 2      60 | 2
        # 42 | 2      30 | 2
        # 21 | 3      15 | 3
        #  7 | 7       5 | 5
        #  1 |         1 |
        
        ALGORYTM EUKLIDESA
        
         NWD(84,60) = NWD(84-60,60) = NWD (24,60) = NWD(24,60-24) = NWD(24,36) =
         = NWD(24,36-24) = NWD(24,12) = NWD(12,12) = 12

        |_______________|__________|___
                        \_________/
        0             a=60   |   b=84
                            b-a
'''

a,b=map(int,input().split())

def nwd(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

print(nwd(a,b))
