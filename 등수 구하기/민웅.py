# 1205_등수구하기_check ranking
import sys
input = sys.stdin.readline

N, record, P = map(int, input().split())

if N > 0:
    score = sorted(list(map(int, input().split())), reverse=True)
else:
    score = []

# 정답 등수 출력을 위한 ans, 배열안에 이미 들어있는 기록수를 체크하기 위한 cnt
ans = 1
# 3 1 3
# 1 1 1 이런 케이스 처리하기 위해서 cnt 필요함
cnt = 1
for i in range(len(score)):
    if ans > P or cnt > P:
        ans = -1
        break
    elif ans == P or cnt == P:
        if score[i] >= record:
            ans = -1
            break
    if score[i] > record:
        ans += 1
        cnt += 1
    elif score[i] == record:
        cnt += 1
    else:
        break

print(ans)