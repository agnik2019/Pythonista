import itertools
lst = [1,2,3,4,5]
sum_list = itertools.accumulate(lst)
print(list(sum_list))