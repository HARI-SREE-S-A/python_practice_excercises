#should return an alphabet which is four more than its original index for  character given
def encrypt(c):
  ref = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  l = []
  for w in c:
    n = ref.index(w)
    s = n + 4
    b = ref[s]
    l.append(b)
  return("".join(l))

