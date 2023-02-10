
nums = [1,2,3,4,5,6]
target = 9
new = sorted(nums)
list = []
h
for i,n in enumerate(nums):
	l = 1
	r = len(nums)-1
	if i > 0 and n == new[i-1]:
		continue
	while l < r:
		summ = n + new[l] + new[r]
		if summ > target:
			l -= 1
		elif summ < target:
			r += 1
		else:
			list.append([n,new[l],new[r]])
			l += 1
			while new[l] == new[l-1] and l < r:
				l += 1
return(list)	
  
