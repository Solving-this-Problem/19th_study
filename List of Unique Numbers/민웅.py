# 13144_List of Unique Numbers
import sys
input = sys.stdin.readline

N = int(input())

sequence = list(map(int, input().split()))

dic = {}
i, j = 0, 0
ans = 0
while j != N:
    if sequence[j] not in dic.keys():
        dic[sequence[j]] = 1
        j += 1
    else:
        while sequence[i] != sequence[j]:
            ans += (j-i)
            if sequence[i] in dic.keys():
                dic.pop(sequence[i])
            i += 1
        j += 1
        i += 1
        ans += (j-i)

while i != N:
    ans += (j-i)
    i += 1
print(ans)