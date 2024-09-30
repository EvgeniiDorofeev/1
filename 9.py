def check_sort(array):
    return all([x > y for x, y in zip(array, array[1:])])
z = [int(i) for i in input().split()]
print(check_sort(z))