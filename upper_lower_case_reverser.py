name = input()
l = []
for n in name:
  if n.isupper():
    l.append(n.lower())
   elif n.islower():
    l.append(n.upper())
b = "".join(l)
return(b)
