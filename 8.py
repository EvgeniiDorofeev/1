sp=list(input().lower().split())
#print(sp)
a=map(lambda x:'a' in x, sp)
print(all(a))