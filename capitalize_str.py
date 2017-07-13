def capitalize(string):
    string.strip()
    li=string.split(" ")
    sli=[]
    for i in li:
        sli.append(i.capitalize())
    return(" ".join(sli))
cap_str=capitalize(input())
print(cap_str)
