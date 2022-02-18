test_case = int(input())
print(test_case)
for c in range(test_case):
    u_input = input()
    u_input = u_input.split(' ')
    bags = int(u_input[0])
    children = int(u_input[1])
    print(bags)
    print(children)
    choco = 0
    temp_c = input()
    temp_c = temp_c.split(' ')
    for cho in temp_c:
        choco += int(cho)
    
    res = choco % children
    print('Case #' + str(c + 1) + ': ' + str(res))
