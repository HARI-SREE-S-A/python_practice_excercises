import string

nm = string.ascii_lowercase[::1]
lisst = []
py = ["p", "y", "t", "h", "o", "n"]


for name in nm:


    with open(name + ".txt", "r") as f:
        m = (f.read().strip("\n"))
        if m in py:
            print("hi")
            lisst.append(m)
        else:
            continue
        f.close()

print(lisst)
