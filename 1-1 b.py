max_num = 10
i = 0
while i < max_num:
    i += 1
    space = max_num - i
    for s in range(space):
        print(" ", end='')
 
    for n in range(1, (max_num - space) + 1):
        print(n, end='')
 
    for n in reversed(range(1, i)):
        print(n, end='')
 
    print("")