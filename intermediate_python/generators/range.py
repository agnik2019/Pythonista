# Lemma : Range is not an iterator
x = range(1,11)
print(x)
#next(x)
#   File "range.py", line 4, in <module>
#     next(x)
# TypeError: 'range' object is not an iterator

print(next(iter(x)))
