# unpacking
tup = (1,2,3,4,5)
lst = [1,2,3,4,5]
string = "hello"
dic = {"a":1,"b":2}
coords = [1,2]

a,b,c,d,e = string
print(a, b, c, d, e)

x, y = coords
print(x,y)


# Multiple assignment
width, height = 400, 500
width, height, x = height, width, 5
print(width, height, x)



# Comprehension
x = [[ 0 for _ in range(5)] for _ in range(5)]
print(x)


sentence = "Hi, My name is Agnik"
x = {char: sentence.count(char) for char in set(sentence)}
print(x)

divby2 = [i for i in range(40) if i%2 == 0]
print(divby2)



# Object Multiplication
x = [5,3]*5
print(x)


# Inline/ternary Conditon
x = 1 if 2>3 else 0
print(x)


# zip
names = ['Agnik','Ayan','Arthi','Amrita','Arijit']
hobbies = ['gardening','listening','shouting','coding','watching']
ages = [22,30,30,25,39]

print(list(zip(names, ages,hobbies)))

for name, age in zip(names,ages):
    if age>29:
        print(name,age)

