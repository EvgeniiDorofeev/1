def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

def trailing_zeros(n):
    if n == 0:  # если введенное число равно нулю - возвращаем 0
        return 0
    else:  # иначе считаем факториал

        k=0
        a=factorial(n)
        s=str(a)[::-1]
        print('fak=',s)
        for i in list(s):

            if i!=0:
                break
            else:
                print('a=', i)
                k=k+1
        print(k)
        return k

# код ниже не стоит удалять, он нужен для проверки
assert trailing_zeros(0) == 0
assert trailing_zeros(6) == 1
assert trailing_zeros(30) == 7
assert trailing_zeros(12) == 2
print('Проверки пройдены')