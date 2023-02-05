def cnt(n):
  c = 0
  while n != 0:
    n  = n//10
    c += 1
  return(c)
def avg(n):
  s = 0
  for i in range(cnt(n)):
    s += n%10
    n = n // 10
  return(s)


l = []
for i,n in enumerate(number):
  l.append(avg(numbers))
max_avg = max(l)
index_max = l.index(max_avg)

return(max_avg,number[index_max]
    

