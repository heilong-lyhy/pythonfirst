#输出100-999之间的所有水仙花数
sxh = set( )
def ceshi(ge,shi,bai):
    chucun = ge^3+shi^3+bai^3
    return chucun
for i in range(100,1000):
    a=int(i/100)
    b=int((i-a*100)/10)
    c=int(i-a*100-b*10)
    
    if(ceshi(a,b,c)==i):
        sxh.add(i)
print(sxh)