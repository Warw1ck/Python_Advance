
my_stack = []

my_commands = {
    1: lambda x: my_stack.append(x[1]),
    2: lambda x: my_stack.pop() if my_stack else None,
    3: lambda x: print(max(my_stack)) if my_stack else None,
    4: lambda x: print(min(my_stack)) if my_stack else None
}

for _ in range(int(input())):
    numbers = [int(x) for x in input().split()]
    my_commands[numbers[0]](numbers)

my_stack.reverse()
print(*my_stack, sep=', ')
