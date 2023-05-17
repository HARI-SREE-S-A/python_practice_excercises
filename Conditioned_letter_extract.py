import string

nm = string.ascii_lowercase[::1]
lisst = []
py = ["p", "y", "t", "h", "o", "n"]

for name in nm:


    with open(name + ".txt", "r") as f:
        print(f.read().strip("\n"))
        if (f.read().strip("\n")) in py:
            print("hi")
            lisst.append(f.read().strip("\n"))
        else:
            continue

print(lisst)

