a = int(input()) # 98
n = a
count = 0
while True:
    b = n // 10 # 9
    c = n % 10 # 8
    b = (b + c) % 10 # 1'7'
    n = (c * 10) + b # 8 * 10 + 7
    count += 1
    if n == a:
        break
print(count) # 60