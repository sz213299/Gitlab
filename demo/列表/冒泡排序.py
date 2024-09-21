x = [8,4,6,67,8,78,65,56]

for i in range(len(x)-1):
    for j in range(i+1,len(x)):
        if x[j]<x[i]:
            x[j],x[i] = x[i],x[j]
print(x)