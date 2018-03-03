import re
n = int(input())

pattern = re.compile('.*I.*E.*E.*E.*-.*S.*J.*C.*E.*')
for i in range(n):
    s = input().strip()
    if(pattern.match(s) is None):
        print('NO')
    else:
        print('YES')
