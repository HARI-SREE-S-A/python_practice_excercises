import string
l = []
k = []

with open("letters.txt","w") as file:
    for letter in string.ascii_lowercase:
        l.append(letter)
        k.append(letter)
q,o = l[::2] ,k[1::2]

for i in range(0,14):
    print(q[i]+o[i])
  
    
   
