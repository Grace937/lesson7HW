q=int(input('學生數量?'))
s=[]
a=0
for i in range (q):
    w=int(input('成績?'))
    s.append(w)
sum=sum(s)
y=sum/q
max=max(s)
min=min(s)
print('最高',max,'最低',min,'平均',y)