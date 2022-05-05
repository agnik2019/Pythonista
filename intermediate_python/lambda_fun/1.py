x ="GeeksforGeeks"
 
# lambda gets pass to print
(lambda x : print(x))(x)

def cube(y):
    return y*y*y
 
lambda_cube = lambda y: y*y*y

print(cube(5))

print(lambda_cube(5))