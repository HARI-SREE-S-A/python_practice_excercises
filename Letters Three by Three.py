import string

a = string.ascii_lowercase[::1]
b = string.ascii_lowercase[1::3]
c = string.ascii_lowercase[2::3]
i = 0
while i < 27:
    try:
        if i == 24:
            print(a[24],a[25])
            break
        else:
            print(a[i]+a[i+1]+a[i+2]+"\n")
        i += 3
    except:
        break





