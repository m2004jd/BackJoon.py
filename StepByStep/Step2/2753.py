a = int(input())
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0: # and : 그리고
    print(1)                                      # or  : 또는
else:
    print(0)