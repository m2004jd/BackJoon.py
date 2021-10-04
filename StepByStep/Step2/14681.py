x, y = map(int, input().split())
if x > 0 and y > 0 :    # x: +, y: +
    print('1')
elif x < 0 and y > 0 :  # x: -, y: +
    print('2')
elif x < 0 and y < 0 :  # x: -, y: -
    print('3')
else:                   # x: +, y: -
    print('4')