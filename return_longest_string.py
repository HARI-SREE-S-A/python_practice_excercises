strng =[str(x) for x in input("enter the strings").split(" ")]
b = []

longest = 0
for n in strng:
    b.append(len(n))

print(strng[b.index(max(b))])


