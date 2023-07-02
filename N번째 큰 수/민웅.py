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
