# 2075 N번째 큰 수
import sys
import heapq
input = sys.stdin.readline

N = int(input())
que = []
for _ in range(N):
    for e in list(map(int, input().split())):
        heapq.heappush(que, e)
        if len(que) > N:
            heapq.heappop(que)
print(heapq.heappop(que))
''' 실패작
heapq 이용
# import sys
# import heapq
# input = sys.stdin.readline

# N = int(input())
# arr = [list(map(int, input().strip().split())) for _ in range(N)]
# que = []
# maxIndex = [N-1] * N
# for idx in range(N):
#     heapq.heappush(que,(-arr[N-1][idx], idx))
# for _ in range(N):
    
#     val, index = heapq.heappop(que)
#     maxIndex[index] -= 1
#     if maxIndex[index] != -1:
#         heapq.heappush(que, (-arr[maxIndex[index]][index], index))
# print(-val)

리스트 이용
# import sys
# input = sys.stdin.readline

# N = int(input())
# arr = [list(map(int, input().strip().split())) for _ in range(N)]
# maxIndex = [N-1] * N
# for _ in range(N):
#     maxI = 0
#     for idx in range(N):
#         if maxIndex[idx] >= 0 and arr[maxIndex[idx]][idx] > arr[maxIndex[maxI]][maxI]:
#             maxI = idx
#     ans = arr[maxIndex[maxI]][maxI]
#     maxIndex[maxI] -= 1
    
# print(ans)
'''