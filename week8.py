seq=[]
while 1:
    a=input()
    if a=="":
        break
    else:
        seq.append(int(a))

Storedbest={}
Storedbest[0]=1
Max=1
for i in range(len(seq)):
    
    for j in range(i):
        if seq[i]%seq[j]==0:
            
            Max=max(Max,Storedbest[j]+1)
            
    Storedbest[i]=Max
    
print(Max)
