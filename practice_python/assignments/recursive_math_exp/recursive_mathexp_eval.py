# /**
#  * @author Vinay Ummadi
#  * @email ummadi.vinay2000@gmail.com
#  * @create date 2022-09-20 20:22:58
#  * @modify date 2022-09-20 20:22:58
#  * @desc [description]
#  */
# ---------------------------------------------



#     """
#     You are given a string containing a math expression.
#     The task is to evaluate the expression using recursion and return the result as an integer.
    
#     Output: Return an integer containing the result of the math expression.
    
#     Hint : Check the inbuilt eval() function and how it works, then you can solve this problem in a single line of code.
#     """
#     # Your code goes here
#     eval(expression)
    
#     return
    
     


# if __name__ == "__main__":
#     print(evaluate_mathexp("1+2*3"))
#     print(evaluate_mathexp("2+3*4^2"))

# def evaluate_mathexp(expression: str) -> int:
# class Solution:
#     def calculate(self, s):
#         def update(op, v):
#             if op == "+": stack.append(v)
#             if op == "-": stack.append(-v)
#             if op == "*": stack.append(stack.pop() * v)           #for BC II and BC III
#             if op == "/": stack.append(int(stack.pop() / v))      #for BC II and BC III
    
#         it, num, stack, sign = 0, 0, [], "+"
        
#         while it < len(s):
#             if s[it].isdigit():
#                 num = num * 10 + int(s[it])
#             elif s[it] in "+-*/":
#                 update(sign, num)
#                 num, sign = 0, s[it]
#             elif s[it] == "(":                                        # For BC I and BC III
#                 num, j = self.calculate(s[it + 1:])
#                 it = it + j
#             elif s[it] == ")":                                        # For BC I and BC III
#                 update(sign, num)
#                 return sum(stack), it + 1
#             it += 1
#         update(sign, num)
#         return sum(stack)
# from re import S

def evaluate_mathexp(expression: str) -> int:
    s= str(expression)

    if len(s)<=3:
        return eval(s)
    else:
        for c in ('+','-','*','/','^'):
            left, operator, right = s.partition(c)
            print(f"{left} -->  {operator} --> {right}")
            if operator == '/':
                return evaluate_mathexp(left) / evaluate_mathexp(right)
            elif operator == '*':
                return evaluate_mathexp(left) * evaluate_mathexp(right)
            elif operator == '+':
                return evaluate_mathexp(left) + evaluate_mathexp(right)
            elif operator == '-':
                return evaluate_mathexp(left) - evaluate_mathexp(right)
            elif operator == '^':
                return evaluate_mathexp(left) ** evaluate_mathexp(right)
    
    return

if __name__ == "__main__":
    #print(evaluate_mathexp("2+3*4"))
    print(evaluate_mathexp("2+3*4 ^ 2"))


    
#     e=eval(s)
#     print(e)

# evaluate_mathexp(3+4)