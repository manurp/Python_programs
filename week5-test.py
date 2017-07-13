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
        if (int(a)>int(b) and int(c)>int(d)) or int(a)<int(b) and int(c)<int(d):
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
        
#print("Number of games won " ,gw)
#print("Number of games lost ",gl)

x5=max(set5.values())
x3=max(set3.values())
xs=max(sw.values())
xg=max(gw.values())
#print(x5)

players={}
play=[]
for i in winners.keys():
    if winners[i] in players.keys():
        j=0
    else:
        players[winners[i]]=0

for i in losers.keys():
    if losers[i] in players.keys():
        j=0
    else:
        players[losers[i]]=0
#print(players)

for i in winners.keys():
    if winners[i] in play:
        j=0
    else:
        play.append(winners[i])
        
for i in losers.keys():
    if losers[i] in play:
        j=0
    else:
        play.append(losers[i])

#print(play)


set5l=sorted(set5,key=set5.get)
set3l=sorted(set3,key=set3.get)
swl=sorted(sw,key=sw.get)
#sll=sorted(sll,key=sll.get)
gwl=sorted(gw,key=gw.get)
#gll=sorted(gll,key=gll.get)
play=set5l


for i in range(len(set5l)-1,0,-1):
    if set5[play[i]]==set5[play[i-1]]:
        for j in range(len(set3l)-1,0,-1):
            if set3[play[j]]==set3[play[j-1]]:
                for k in range(len(swl)-1,0,-1):
                    if sw[play[k]]==sw[play[k-1]]:
                        for h in range(len(gwl)-1,-1,-1):
                            if gw[play[k]]<gw[play[k-1]]:
                                (play[k],play[k-1])=(play[k-1],play[k])
                    elif sw[play[j]]<sw[play[j-1]]:
                        (play[j],play[j-1])=(play[j-1],play[j])
            elif set3[play[i]]<set3[play[i-1]]:
                (play[i],play[i-1])=(play[i-1],play[i])
    
for i in range(len(set5l)-1,-1,-1):
    print(play[i],set5[play[i]],set3[play[i]],sw[play[i]],gw[play[i]],sl[play[i]],gl[play[i]])
                            
