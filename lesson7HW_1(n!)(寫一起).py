n=int(input('幾階?'))
def a(n):
    y=0
    for j in range(1,n+1):
        d=1
        for i in range(1,j+1):
            d=d*i
        y=d+y
    return y

print(a(n))

