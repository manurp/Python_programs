first= []
while True:
    line=input("")
    if line=="":
        break
    else:
        first.append(line)
        
main={}
winners={}
losers={}
sets={}
games={}
set5={}
set3={}
sw={}
sl={}
gw={}
gl={}
if '\t'in first:
    first.remove('\t')
for i in range(len(first)):
    main[i]=first[i].split(":")[:2]

for i in range(len(first)):
    x=first[i].split(":")[2]
    games[i]=x.split(",")

#print(games)
#print(main)
    

for i in main.keys():
    winners[i]=main[i][0]
    
#print(winners)

for i in main.keys():
    losers[i]=main[i][1]

#print(losers)

for i in winners.keys():
    set3[winners[i]]=0
    set5[winners[i]]=0
    
for i in losers.keys():
    set3[losers[i]]=0
    set5[losers[i]]=0
    
for i in games.keys():
    if len(games[i])<3:
        set3[winners[i]]+=1
    elif len(games[i])>3:
        set5[winners[i]]+=1
    if len(games[i])==3:
        a=games[i][0].split("-")[0]
        b=games[i][0].split("-")[1]
        c=games[i][1].split("-")[0]
        d=games[i][1].split("-")[1]
        if (int(a)>int(b) and int(c)>int(d)):
            set5[winners[i]]+=1
        else:
            set3[winners[i]]+=1

#print("Best of 5 set Won ",set5)
#print("Best of 3 set won ",set3)

for i in losers.keys():
    sw[losers[i]]=0
    sl[losers[i]]=0

for i in winners.keys():
    sw[winners[i]]=0
    sl[winners[i]]=0

for i in games.keys():
    for j in range(len(games[i])):
        a=games[i][j].split("-")[0]
        b=games[i][j].split("-")[1]
        if int(a) > int(b):
            sw[winners[i]]+=1
            sl[losers[i]]+=1
        else:
            sw[losers[i]]+=1
            sl[winners[i]]+=1

#print("Number of sets won ",sw)
#print("Number of sets lost ",sl)

for i in losers.keys():
    gw[losers[i]]=0
    gl[losers[i]]=0

for i in winners.keys():
    gw[winners[i]]=0
    gl[winners[i]]=0
    
for i in games.keys():
    for j in range(len(games[i])):
        a=games[i][j].split("-")[0]
        b=games[i][j].split("-")[1]
        gw[winners[i]]+=int(a)
        gl[losers[i]]+=int(a)
        gl[winners[i]]+=int(b)
        gw[losers[i]]+=int(b)
        
play=[]

for i in winners.keys():
    if winners[i] not in play:
        play.append(winners[i])
        
for i in losers.keys():
    if losers[i] not in play:
        play.append(losers[i])

#print(play)


play=sorted(set5,key=set5.get)
#print(play)
j=len(play)
while j>0:

    for i in range(len(play)-1,0,-1):
        if set5[play[i]]==set5[play[i-1]]:
            if set3[play[i]]==set3[play[i-1]]:
                
                if sw[play[i]]==sw[play[i-1]]:
        
                    if gw[play[i]]<gw[play[i-1]]:
                        (play[i],play[i-1])=(play[i-1],play[i])
                        
                elif sw[play[i]]<sw[play[i-1]]:
                    (play[i],play[i-1])=(play[i-1],play[i])
                    
            elif set3[play[i]]<set3[play[i-1]]:
                (play[i],play[i-1])=(play[i-1],play[i])
                
    j-=1
    
for i in range(len(play)-1,-1,-1):
    print(play[i],set5[play[i]],set3[play[i]],sw[play[i]],gw[play[i]],sl[play[i]],gl[play[i]])
                            
