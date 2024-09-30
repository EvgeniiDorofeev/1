words = input().split()

found = False
for word in words:
    if word.lower().endswith('ought'):
        found = True
        break

print(found)