x=[1,1,2,8,3,2,3,4,0,5,7,6,8,9,9]
l1=[]
for i in x:
        if i not in l1:
            if x.count(i)==1:
                l1.append(i)
print(l1)
