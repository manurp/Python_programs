def orangecap(d):
    total={}
    for match in d.keys():
        for n in d[match].keys():
            total[n]=0
    for match in d.keys():
        for n in d[match].keys():
            total[n]=total[n]+d[match][n]
    score=list(total.values())
    players=list(total.keys())
    i=max(score)
    ind=score.index(i)
    player=players[ind]
    return(player,i)
def sort(a,l,r):
    if r-l<=1:
        return()
    i=l+1

    for j in range(l+1,r):
        if(a[j][1]>a[l][1]):
           (a[i],a[j])=(a[j],a[i])
           i=i+1

    (a[l],a[i-1])=(a[i-1],a[l])

    sort(a,l,i-1)
    sort(a,i,r)
def addpoly(p1,p2):
    pn=[]
    l=len(p2)
    
    for i in range(len(p1)):
                 j=0
                 k=0
                 while j<l:
                     
                     if p1[i][1]==p2[j][1]:
                         k=k+1
                         if p1[i][0]+p2[j][0]!=0:
                             pn.append((p1[i][0]+p2[j][0],p1[i][1]))
                         p2.remove(p2[j])
                         l=l-1
                         j=j-1
                     j=j+1        
                 if k==0:
                         pn.append(p1[i])
                     
    pn=pn+p2
    sort(pn,0,len(pn))
    return(pn)
def multpoly(p1,p2):
    d={}
    if len(p2)<len(p1):
        (p1,p2)=(p2,p1)
    for i in range(len(p1)):
        p=[]
        for j in range(len(p2)):
            x=p1[i][0]*p2[j][0]
            y=p1[i][1]+p2[j][1]
            p.append((x,y))
        d[i]=p
    res=resdict(d)
    j=0
    l=len(res)
    while j<l:
        if res[j][0]==0:
            res.remove(res[j])
            l=l-1
            j=j-1
        j=j+1
    return(res)

def resdict(d):
    d1={}
    
    if len(d)<=1:
        for k in d.keys():
            return(list(d[k]))
    
    else:
        j=0
        for i in range(0,len(d),2):
            d1[j]=addpoly(d[i],d[i+1])
            j=j+1
        return(resdict(d1))
