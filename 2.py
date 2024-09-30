n=int(input())
def gen_fibonacci_numbers(n):
    f1 = 1
    f2 = 1
    for i in range(1,n+1):
        if i<2:
            yield 1
        else:
            yield f2
            f1, f2=f2, f1+f2

for i in gen_fibonacci_numbers(n):
    print(i)