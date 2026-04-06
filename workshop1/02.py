def sort_stack(stack):
    stack_dop = []

    while stack:
        temp = stack.pop()

        while stack_dop and stack_dop[-1] < temp:
            stack.append(stack_dop.pop())
        stack_dop.append(temp)

    return stack_dop


stack = [6, 1, 5, 4, 3, 2]  
print(sort_stack(stack))
print(sort_stack(stack).pop())

stack = [6, -1, -1, -1, 1, 5, 4, 3, 2]  
print(sort_stack(stack))
print(sort_stack(stack).pop())