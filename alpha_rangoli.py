

def print_rangoli(size):
    m=(size-1)*2
    #print(m)
    s="a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z"
    s=s[:m+1]
    #print(s)
    for i in range(m,0,-2):
        st=s[:i:-1]+s[i:]
        print(st.center(m*2+1,'-'))
    st=s[:0:-1]+s
    print(st)
    for i in range(2,m+1,2):
        st=s[:i:-1]+s[i:]
        print(st.center(m*2+1,'-'))

n=int(input())
print_rangoli(n)
