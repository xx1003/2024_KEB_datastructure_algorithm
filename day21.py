# import webbrowser
# import time
# def is_stack_full():
#     global size, stack, top
#     if top >= size - 1:
#         return True
#     else:
#         return False
#
#
# def is_stack_empty():
#     global size, stack, top
#     if top == -1:
#         return True
#     else:
#         return False
#
#
# def push(data):
#     global size, stack, top
#     if is_stack_full():
#         print("Stack is Full")
#         return
#     top += 1
#     stack[top] = data
#
#
# def pop():
#     global size, stack, top
#     if is_stack_empty():
#         print("Empty stack")
#         return None
#     data = stack[top]
#     stack[top] = None
#     top -= 1
#     return data
#
#
# def peek():
#     global size, stack, top
#     if is_stack_empty():
#         print("Empty stack")
#         return None
#     else:
#         return stack[top]

def checkBracket(expr: str) -> bool:
    """
    check bracket in expression
    :param expr: str
    :return: bool
    """
    stack = list()
    table = {')': '(', ']': '[', '}': '{', '>': '<'}
    for char in expr:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
        else:
            pass
    return len(stack) == 0

## 메인 코드 부분 ##
if __name__ == "__main__":
    expression = input("Input expression : ")
    print(checkBracket(expression))
