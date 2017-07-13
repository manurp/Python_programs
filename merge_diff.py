def merge_diff(a,b):
    (m,n,c)=(len(a),len(b),[])
    k=0
    while k<m:
        temp=m
        for h in range(n):
            if a[k]==b[h]:
                a.remove(a[k])
                m=m-1
            if m==0:
                break
        if m==temp:
            k=k+1
    return(a)
