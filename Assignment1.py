i=[1,2,1,3,2,3,4,0,5,6,3,4,3,6.8]
l1=[]
l2=[]
for i in x:
    if i%2==1:
        if i not in l1:
            l1.append(i)
            l2.append(x.count(i))
print(l1)
print(l2)
