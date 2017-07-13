for i in range(1,int(input())+1):
    print  (reduce(lambda x, y: x + (10 ** (y - 1)), range(1, i + 1))**2) #reduce works for python2