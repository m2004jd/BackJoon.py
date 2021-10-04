a, b = map(int, input().split())
c = list(map(int, input().split())) # c라는 배열의 index값에 입력
for i in range(a):
    if c[i] < b:                    # c[index]가 b보다 작다면 이라는 조건문
        print(c[i], end=' ')