n = int(input())
left_right = []
left = []
right = []
result = ''
for i in range(n):
    result = input()
    if result == '(' or result == ')':
        left_right.append(result)
    if result == '(':
        left.append('(')
    if result == ')':
        right.append(')')

if len(left) == len(right):
    for i in range(0, len(left_right), 2):
        if left_right[i] != '(':

            print('UNBALANCED')
            break
    else:
        print('BALANCED')
else:
    print('UNBALANCED')
