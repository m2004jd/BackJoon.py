h, m = map(int, input().split())
if m >= 45:                 # m이 45 이상일때
    print(h, m - 45)
elif h > 0 and m < 45:      # m이 45 미만일때
    print(h - 1, m + 15)
else:                       # h이 0 일때
    print(23, m + 15)
