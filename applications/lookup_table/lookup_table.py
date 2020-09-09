# Your code here
import random
import math
import timeit


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


cache_dict = {}


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here

    key_ = str(x) + ','+str(y)
    if key_ in cache_dict:
        # print("used cache")
        return cache_dict[key_]
    else:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        cache_dict[key_] = v
        return v


# Do not modify below this line!
start_time = timeit.default_timer()
for i in range(50000):  # 50000
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    slowfun(x, y)
    # print(f'{i}: {x},{y}: {slowfun(x, y)}')

elapsed = timeit.default_timer() - start_time
print(f'done {elapsed}')
