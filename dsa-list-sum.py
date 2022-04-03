def list_sum(data_list):
    x = 0
    for i in data_list:
        if type(i) == type([]):
            x = x+list_sum(i)

        else:
            x = x+i
    return x
print(list_sum([1, 2, [3,4],[5,6]]))
