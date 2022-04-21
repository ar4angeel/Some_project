import random

def pinetree():
    n = 10
    tree = [
        ' '*(n-i)+'/'+''.join(random.choice(' # *')
        for _ in range(2*i))+'\\'
        for i in range(n)
    ]

    print('\n'.join(tree))

def calculator(a):
    empty_num_list = []
    empty_operator_list = []
    for i in a:
        empty_num_list.append(i)
    print(empty_num_list)



if __name__ == '__main__':
    calculator(input())