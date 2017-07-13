rows=int(input("Enter the number of rows: "))
for i in range(rows):
	val=1
	#print(i,rows)
	for j in range(1,rows-i):
		print("    ",end='')
	for k in range(i+1):
		print("      ",val,end="")
		val=int(val*(i-k)/(k+1))
	print("\n")