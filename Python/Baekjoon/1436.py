# 영화감독 숌(https://www.acmicpc.net/problem/1436)

n = int(input())

name = 666
cnt = 0
while (True):
    if "666" in str(name):
        cnt += 1
        if cnt == n:
            print(name)
            break
    name += 1