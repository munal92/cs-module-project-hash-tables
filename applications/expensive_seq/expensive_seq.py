# Your code here

cache_dict = {}


def expensive_seq(x, y, z):
    key_ = str(x) + ','+str(y)+','+str(z)
    if key_ in cache_dict:
        #print("used cache")
        return cache_dict[key_]
    elif x <= 0:
        res1 = y+z
        cache_dict[key_] = res1
        return res1
    elif x > 0:
        res2 = expensive_seq(x-1, y+1, z) + expensive_seq(x-2,
                                                          y+2, z*2) + expensive_seq(x-3, y+3, z*3)
        cache_dict[key_] = res2
        return res2


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
