d = int(input())

for i in range(d):
    a, b = map(int, input().split())
    if a % b < 0:
        if b > 0:
            print(a%-b)
        else:
            print(a%b)
    else:
        print(a%b)
'''
            ??? Coś źle ???
'''