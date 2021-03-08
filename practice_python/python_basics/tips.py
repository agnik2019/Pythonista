condition = True
# if condition:
#     x = 1
# else:
#     x = 0
# print(x)
x = 1 if condition else 0
print(x)

#big integer addition
num1 = 10_000_000_000
num2 = 10_000_000
total = num1+num2
print(f'{total:,}')

###opening and closing files
# f = open('test.txt','r')
# file_contents = f.read()
# f.close()

with open('test.txt','r') as f:
    file_contents = f.read()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)

