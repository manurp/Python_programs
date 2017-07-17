def onceInATram(x):
	res = x+1
	while( sum(map(int,str(res)[:3])) != sum(map(int,str(res)[3:]))):
		res += 1
	return res

if __name__ == '__main__':
	x = int(input().strip())
	result = onceInATram(x)
	print(result)