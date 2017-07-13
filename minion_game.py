def minion_game(string):
    (s,k)=(0,0)
    l=len(string)
    for i in range(len(string)):
        #print(i)
        #print(string)
        if string[i] not in "AEIOU":
            s+=l-i
        else:
            k+=l-i
        #string=string[i+1:]
        #l-=1
    if s==k:
        print("Draw")
    elif s>k:
        print("Stuart",s)
    else:
        print("Kevin",k)

s=input()
minion_game(s)
