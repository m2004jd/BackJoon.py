a, b = map(int, input().split())
print(b % 10 * a, b % 100 // 10 * a, b // 100 * a, b * a)
