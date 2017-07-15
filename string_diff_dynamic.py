def solve(mid,l,s):
	for i in range(mid,l+1):
		for j in range(mid,l+1):
			tmp = d[i][j]-d[i-mid][j-mid]
			if tmp<=s:
				return True
	return False
def string_diff(p,q,s):
	global d 
	d= dict()
	l = len(p)
    # for i in range(l+1):

	for i in range(l+1):
		d[i] = dict()
		d[0][i] = 0
		d[i][0] = 0
	# print(d)

	for i in range(l):
		for j in range(l):
			if p[i] == q[j] :
				d[i+1][j+1] = d[i][j]
			else:
				d[i+1][j+1] = d[i][j]+1

	low,high = 0,l

	while(low<high):
		mid = (low+high+1)//2
		if(solve(mid,l,s)): low = mid
		else: high = mid-1

	return(low)
with open('string_diff-test-case.txt','r') as fh:
	for line in fh:
		it = int(line.rstrip())
		break
	for i in range(it):
		for line in fh:
			# print(line)
			s,p,q = line.split()
			print(string_diff(p,q,int(s)))
# for _ in range(int(input())):
#     s,p,q = input().split()
#     print(string_diff(p,q,int(s)))