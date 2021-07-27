n=int(input('幾階?'))
def a(a):
    b=1
    for i in range(1,x+1):
        b=b*i
    return b
y=0
for x in range(1,n+1):
    y=a(n)+y
print(y)