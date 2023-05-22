l = []
arr1 = [1, 3, 4, 6, 7, 9]
arr2 = [1, 2, 4, 5, 9, 10]

new = arr1 + arr2

for n in new:
    if new.count(n) == 2 and n  not in l:
        l.append(n)
