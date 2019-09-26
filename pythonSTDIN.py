def get_input_stacks():
    n = int(input())
    stacks = []
    for _ in range(n):
        str_stack = input().split(' ')
        stack = [int(s) for s in str_stack]
        stacks.append(stack)
    return stacks
