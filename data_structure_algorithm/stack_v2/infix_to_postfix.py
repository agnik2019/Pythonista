priority = {
    '/':1,
    '*':1,
    '+':0,
    '-':0,
    '(':-1
}

def infix_to_postfix(infix):
    postfix = []
    st = []
    for token in infix:
        if token == '(':
            st.append(token)
        elif token == ')':
            while st[-1] != '(':
                postfix.append(st.pop())
            st.pop()
        elif token not in "()*/+-":
            st.append(token)
        else:
            while st and priority[st[-1]] >= priority[token]:
                postfix.append(st.pop())
            st.append(token)
        while st:
            postfix.append(st.pop())
    return postfix

infix = "a+b/c*d-e"
print(infix_to_postfix(infix))
