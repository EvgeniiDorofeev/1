n = input()
x=input()
letters = [0]*n
for i in x:
    nomer = int(i)
    letters[nomer] += 1
for i in range(10):
    if letters[i] > 0:
        print(i, letters[i])