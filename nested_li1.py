students=[]
for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        
(flow,slow)=(100,100);
for i in range(len(students)):
    if(flow>students[i][1]):
        (flow,slow)=(students[i][1],flow)
    elif(slow>students[i][1] and flow !=students[i][1]):
        slow=students[i][1]
li=[]
di=dict(students)
for key in di.keys():
    if di[key] ==slow:
        li.append(key)
li.sort()
for na in li:
    print(na)