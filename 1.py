n=int(input())
def gen_squares(n):
    for i in range(1,n+1):
        yield i**2

for i in gen_squares(n):
    print(i)