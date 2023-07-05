# 19th_study
[19주차] 코딩테스트 준비 7주차

[백준 문제집](https://www.acmicpc.net/workbook/view/16000)

[프로그래머스 문제](https://school.programmers.co.kr/learn/courses/30/lessons/150369)

<br/><br/>

# 택배 배달과 수거하기

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [동우](./%ED%83%9D%EB%B0%B0%20%EB%B0%B0%EB%8B%AC%EA%B3%BC%20%EC%88%98%EA%B1%B0%ED%95%98%EA%B8%B0/%EB%8F%99%EC%9A%B0.py)
```py
```

## [민웅](./%ED%83%9D%EB%B0%B0%20%EB%B0%B0%EB%8B%AC%EA%B3%BC%20%EC%88%98%EA%B1%B0%ED%95%98%EA%B8%B0/%EB%AF%BC%EC%9B%85.py)
```py
def solution(cap, n, deliveries, pickups):
    ans = 0
    d_cnt, p_cnt = 0, 0
    for i in range(n-1, -1, -1):
        if deliveries[i] or pickups[i]:
            d_cnt += deliveries[i]
            p_cnt += pickups[i]
            while d_cnt > 0 or p_cnt > 0:
                d_cnt -= cap
                p_cnt -= cap
                ans += 2*(i+1)
        else:
            continue
    return ans
# 테케 맞고 정답은 몇개 틀린코드
#def solution(cap, n, deliveries, pickups):
#     ans = 0
#     for i in range(n-1, -1, -1):
#         if deliveries[i] != 0:
#             idx = i
#             cap_size = cap
#             cap_size2 = cap
#             while idx != -1:
#                 if cap_size >= deliveries[idx]:
#                     cap_size -= deliveries[idx]
#                     deliveries[idx] = 0
#                 else:
#                     deliveries[idx] -= cap_size
# 
#                 if cap_size2 >= pickups[idx]:
#                     cap_size2 -= pickups[idx]
#                     pickups[idx] = 0
#                 else:
#                     pickups[idx] -= cap_size2
#                 idx -= 1
#             ans += 2*(i+1)
# 
#         elif pickups[i] != 0:
#             idx = i
#             cap_size = cap
#             cap_size2 = cap
#             while idx != -1:
#                 if cap_size >= deliveries[idx]:
#                     cap_size -= deliveries[idx]
#                     deliveries[idx] = 0
#                 else:
#                     deliveries[idx] -= cap_size
# 
#                 if cap_size2 >= pickups[idx]:
#                     cap_size2 -= pickups[idx]
#                     pickups[idx] = 0
#                 else:
#                     pickups[idx] -= cap_size2
#                 idx -= 1
#             ans += 2*(i+1)
# 
#     return ans

```

## [서희](./%ED%83%9D%EB%B0%B0%20%EB%B0%B0%EB%8B%AC%EA%B3%BC%20%EC%88%98%EA%B1%B0%ED%95%98%EA%B8%B0/%EC%84%9C%ED%9D%AC.py)
```py
```

## [성구](./%ED%83%9D%EB%B0%B0%20%EB%B0%B0%EB%8B%AC%EA%B3%BC%20%EC%88%98%EA%B1%B0%ED%95%98%EA%B8%B0/%EC%84%B1%EA%B5%AC.py)
```py
```

## [혜진](./%ED%83%9D%EB%B0%B0%20%EB%B0%B0%EB%8B%AC%EA%B3%BC%20%EC%88%98%EA%B1%B0%ED%95%98%EA%B8%B0/%ED%98%9C%EC%A7%84.py)
```py
```

</div>
</details>
<br/><br/>

# 등수 구하기

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [동우](./%EB%93%B1%EC%88%98%20%EA%B5%AC%ED%95%98%EA%B8%B0/%EB%8F%99%EC%9A%B0.py)
```py
import sys
input = sys.stdin.readline

N, score, P = map(int, input().strip().split())

if N:
    scores = list(map(int, input().strip().split())) + [0]      # 랭킹 리스트보다 넘치는지 확인하기 위해서 0 추가!

    rank = 1
    for i in range(len(scores)):
        if i == P:                              # 랭킹 리스트에 올라갈 수 없으면 -1 출력
            rank = -1
        else:
            if scores[i] > score:               # 랭킹 매기기
                rank += 1
            elif scores[i] == score:
                pass
            else:                               # 작은 숫자 만나면 그만 돌아
                break
    print(rank)
else:
    print(1)
```

## [민웅](./%EB%93%B1%EC%88%98%20%EA%B5%AC%ED%95%98%EA%B8%B0/%EB%AF%BC%EC%9B%85.py)
```py
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
```

## [서희](./%EB%93%B1%EC%88%98%20%EA%B5%AC%ED%95%98%EA%B8%B0/%EC%84%9C%ED%9D%AC.py)
```py
```

## [성구](./%EB%93%B1%EC%88%98%20%EA%B5%AC%ED%95%98%EA%B8%B0/%EC%84%B1%EA%B5%AC.py)
```py
```

## [혜진](./%EB%93%B1%EC%88%98%20%EA%B5%AC%ED%95%98%EA%B8%B0/%ED%98%9C%EC%A7%84.py)
```py
```

</div>
</details>
<br/><br/>


# N번째 큰 수

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [동우](./N%EB%B2%88%EC%A7%B8%20%ED%81%B0%20%EC%88%98/%EB%8F%99%EC%9A%B0.py)
```py
import sys, heapq
input = sys.stdin.readline

N = int(input().strip())

heap = []                                   
for _ in range(N):
    arr = list(map(int, input().strip().split()))

    if not heap:                            # heap이 비어있다면 채워준다. 처음에만 해당
        for i in arr:
            heapq.heappush(heap, i)         # min_heap 구조로 heap 채워준다
    else:
        for i in arr:
            if i > heap[0]:                 # heap의 최소값(n번째로 큰 수)보다 새로운 값이 더 크면 
                heapq.heappush(heap, i)     # push해주고
                heapq.heappop(heap)         # 최솟값은 pop해준다

print(heap[0])
```

## [민웅](./N%EB%B2%88%EC%A7%B8%20%ED%81%B0%20%EC%88%98/%EB%AF%BC%EC%9B%85.py)
```py
# 2075_N번째 큰 수_Nth number
# 한 번에 맞았지만, 비효율적인것 같음.
import sys
import heapq
input = sys.stdin.readline

N = int(input())

numbers = sorted(list(map(int, input().split())), reverse=True)
for _ in range(N-1):
    lst = list(map(int, input().split()))
    for i in range(N):
        heapq.heappush(numbers, lst[i])
        heapq.heappop(numbers)

print(numbers[0])

```

## [서희](./N%EB%B2%88%EC%A7%B8%20%ED%81%B0%20%EC%88%98/%EC%84%9C%ED%9D%AC.py)
```py
```

## [성구](./N%EB%B2%88%EC%A7%B8%20%ED%81%B0%20%EC%88%98/%EC%84%B1%EA%B5%AC.py)
```py
```

## [혜진](./N%EB%B2%88%EC%A7%B8%20%ED%81%B0%20%EC%88%98/%ED%98%9C%EC%A7%84.py)
```py
```

</div>
</details>

<br/><br/>

# List of Unique Numbers

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [동우](./List%20of%20Unique%20Numbers/%EB%8F%99%EC%9A%B0.py)
```py
```

## [민웅](./List%20of%20Unique%20Numbers/%EB%AF%BC%EC%9B%85.py)
```py
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
```

## [서희](./List%20of%20Unique%20Numbers/%EC%84%9C%ED%9D%AC.py)
```py
```

## [성구](./List%20of%20Unique%20Numbers/%EC%84%B1%EA%B5%AC.py)
```py
```

## [혜진](./List%20of%20Unique%20Numbers/%ED%98%9C%EC%A7%84.py)
```py
```

</div>
</details>
