N = int(input())
nums = [int(x) for x in input().split()]
t = 1

for n in nums:
  prod  = (prod*n)%(10**9 + 7)

  
print(prod)
  
