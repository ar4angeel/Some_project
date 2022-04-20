import random
n = 10
tree = [
    ' '*(n-i)+'/'+''.join(random.choice(' # *')
    for _ in range(2*i))+'\\'
    for i in range(n)
]

print('\n'.join(tree))