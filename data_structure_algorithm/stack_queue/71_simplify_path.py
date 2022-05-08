"""
input : "/foo/../test/../test/../foo//bar/./baz"
output: "/foo/bar/baz

edge cases:
1. /foo////bar/./baz   -> /foo/bar/baz
2. ../../foo   -> ../../foo
3. /../../foo  ->  /foo
4. foo/../bar/baz   -> absolute path


algorithm :
1. first split the path by '/'  -> tokens = ["",foo,"..","test","..","foo","bar",".","baz"]
2. Filter the token by removing "" & "."  -> tokens = [foo,"..","test","..","foo","bar","baz"]
3. if we see ".." , we pop the top of the stack   -> stack = ["foo","bar","baz"]
4. join the stack elements by '/'   ->  result : "/foo/bar/baz"

"""

def simplifyPath(path):
    startsWithSlash = path[0] == "/"
    tokens = filter(isImportant, path.split('/'))
    stack = []
    if startsWithSlash:
        stack.append("")
    for token in tokens:
        if token == "..":
            if len(stack)==0 or stack[-1]=="..":
                stack.append(token)
            elif stack[-1] != "":
                stack.pop()
        else:
            stack.append(token)

    if len(stack) == 1 and stack[0] == "":
        return '/'
    return '/'.join(stack)

def isImportant(token):
    return len(token)>0 and token !="."

def main():
    ans = simplifyPath("/foo/../test/../test/../foo//bar/./baz")
    print(ans)

main()
