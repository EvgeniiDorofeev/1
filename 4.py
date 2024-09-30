str=list(map(str, input().split()))
strings=list(map(lambda x: x, str))
a=[]
for i in strings:
    s=tuple(i.upper()+i.lower())
    a.append(s)
print(a)