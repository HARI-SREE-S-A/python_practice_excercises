d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
print("a has the quantity of  ",d["a"])



#############################################

d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
for key,values in d.items():
    print(key,"has items",values)
