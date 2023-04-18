a = [1, 2, 3]
b = (4, 5, 6)

x = []

for i in range(0,3):
    x.append(a[i]+b[i])
for m in x:
    print(m)
##########

for i,j in zip(a,b):
    print(i+j)

