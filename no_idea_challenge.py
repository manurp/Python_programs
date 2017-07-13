from collections import Counter
def no_idea(m,n,arr,a,b):
    sarr=set(arr)
    h=0
    if len(sarr)==m:
        s=a^b
        s1=sarr.intersection(s)
        if len(s1)==2*n:
            return 0
        else:
            h+=len(s1.intersection(a))
            h-=len(s1.intersection(b))
            return h
    else:
        d=dict(Counter(arr))
        for i in d.keys():
            if i in a:
                h+=d[i]
            elif i in b:
                h-=d[i]
        return h
        
    
m,n=map(int,input().split())
arr=list(map(int,input().split()))
a=set(list(map(int,input().split())))
b=set(list(map(int,input().split())))
print(no_idea(m,n,arr,a,b))
