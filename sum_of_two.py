# given number should be expressed as sum of two integers
def summ(n):
  diff = n - int(n//2)
  if diff <=0:
    return 0
  return (diff,n-diff)
