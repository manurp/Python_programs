def search(ele,list): 
  for i in range(0,len(list)):
      if(ele==list[i]):
        return(i)
  return(-1)
       
def max(list):
 max=list[0]
 for i in range(0,len(list)):
   if(max<=list[i]):
     max=list[i]
   #else:
    # max=list[i]
 return(max)

#l[0]=match1
#score["Test1"]["Dhawan"] = 84

def orangecap(l):
  p=-1
  name=[]
  score=[]
  for k in sorted(l.keys()):                                                       #l[k] is match1,match2
   for m in sorted(l[k].keys()):                                                   #l[k][m] is runs 
                                                                                          
    if search(m,name) is -1:
      name.append(m)
      score.append(l[k][m])
    else:
      score[search(m,name)]=score[search(m,name)]+int(l[k][m])

  #return(name,score)
  #for j in range(0,len(score)):
  # for i in range(0,len(score)-1)
   # if(score[i]<=score[i+1]):
   #   (score(i),score(i+1))=(score(i+1),score(i))
  return(name[search(max(score),score)],score[search(max(score),score)])  
  #return(max(score))
  
  
def common(list,power):
  sum=0
  for i in range(0,len(list)):
    if(list[i][1] is power):
      sum=sum+list[i][0]
  return(sum)
  
def multpoly(p1,p2):
  m=[]
  final=[]
  total=[]
  exp1=p1[0][1]
  exp2=p2[0][1]
  p11=exp1
  p22=exp2
  for i in range(0,len(p1)):
    for j in range(0,len(p2)):
      m.append(((p1[i][0]*p2[j][0]),(p1[i][1]+p2[j][1])))
  #print( m)    
  #for i in range(0,exp1):
    #for j in range(0,exp2):
  n=p11+p22
  while(n>=0):
    total=common(m,n)
    #print(total)
    if(total is not 0):
     final.append((total,n))
    n=n-1   
  return(final)  
      
#addpoly([(4,3),(3,0)],[(-4,3),(2,1)])
#[(2, 1),(3, 0)]        
def maximum(n,m):
  if(n>=m):
   return(n)
  else:
   return(m)
  
def addpoly(p1,p2):
  final=[]
  total=[]
  exp1=p1[0][1]
  exp2=p2[0][1]
  p1.extend(p2)
  n=exp1+exp2
  while(n>=0):
    total=common(p1,n)
    #print(total)
    if(total is not 0):
     final.append((total,n))
    n=n-1
  return(final)  
   
