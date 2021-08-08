# args and kargs

def fun1(arg1, arg2, arg3):
    print(arg1, arg2, arg3)

def fun2(arg1= None, arg2 = None, arg3 = None):
    print(arg1, arg2, arg3)

args = [1,2,3]
fun1(*args)

kargs = {'arg2':2,'arg1':1,'arg3':3}
fun2(**kargs)