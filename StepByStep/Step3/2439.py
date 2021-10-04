a = int(input())
for i in range(1, a + 1):
	print(' ' * (a - i) + '*' * i)
# 공백을 a-i만큼 출력 이러서 *을 i만큼 출력