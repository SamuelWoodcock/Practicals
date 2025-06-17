
for i in range(1, 21, 2):
    print(i, end=' ')
print()
#a
for x in range(0,110,10):
    print(x, end= ' ')
    print()
#b
for y in range(20,0,-1 ):
    print(y, end=' ')
    print()
#c Printing n stars
n=int(input("Number of stars: "))
for _ in range(n):
    print('*', end= '')
    print()

#d
for i in range(1,n+1):
    print('*'* i)
