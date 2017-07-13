def fib(n):
    while 1:
        try:
            n=int(n)
            (first,second)=(1,1)
            if n>=1:
                print(first,end=" ")
            if n>=2:
                print(second,end=" ")
            if n>=3:
                for i in range(2,n):
                    nextv=first+second
                    print(nextv,end=" ")
                    (first,second)=(second,nextv)
                
            break
        except ValueError:
            n=input("Enter a valid integer:\n")
