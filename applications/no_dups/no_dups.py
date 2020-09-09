def no_dups(s):
    # Your code here
    word = s.split()
    dict_arr = {}
    for i in word:
        if i not in dict_arr:
            dict_arr[i] = 1
        else:
            dict_arr[i] += 1
    return ' '.join(dict_arr.keys())


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
