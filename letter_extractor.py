import string
nm = string.ascii_lowercase[::1]
lisst = []

for name in nm:


    with open(name + ".txt","r") as f:
        lisst.append(f.read().strip("\n"))


print(lisst)

