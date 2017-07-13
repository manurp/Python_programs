def merge_the_tools(string, k):
    t=[]
    for i in range(0,len(string),k):
        t.append(string[i:i+k])
    for i in t:
        st=""
        for j in i:
            if j not in st:
                st+=j
        print(st)
string,k=input(),int(input())
merge_the_tools(string,k)