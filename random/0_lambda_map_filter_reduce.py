def odd_num(x):
    return (x % 2)
def list_odd(func, my_list):
    return [x for x in my_list if func(x)]
my_list = [1,2,3,4,5,6,7,8,9]

print(list_odd(odd_num, my_list))

import random

def count_h_t(my_list):
    Heads = 0
    Tails = 0
    for x in my_list:
        if x == 'H':
            Heads += 1
        else:
            Tails += 1
    return (Heads, Tails)

h_t_list = []
ht = ['H', 'T']
for _ in range(50):
    h_t_list.append(random.choice(ht))
Heads, Tails = count_h_t(h_t_list)
print("Heads: ", Heads)
print("Tails: ", Tails)

def multiple_9(my_list):
    return list(filter(lambda x: x % 9 == 0, my_list))
print(multiple_9(range(1, 1000)))

from functools import reduce
print(reduce((lambda x, y: x + y), range(1, 6)))
