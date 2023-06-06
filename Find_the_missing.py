# finding the missing number

n = [int(c) for c in input("enter the number with space").split(" ")]

n = sorted(n)

for x in range(n[1],n[-1]+1):
    if x not in n:
        print(x)

