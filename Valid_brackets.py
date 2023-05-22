s = "{[(])}"

d = {"]":"[",")":"("}

stack  =[]
for c in s:
    if c in d :
        if stack and stack[-1] == d[c]:
            stack.pop()
        else:
            print(False)
    else:
        stack.append(c)
print(True) if not stack else print(False)


