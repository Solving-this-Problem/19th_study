import sys, heapq

input = sys.stdin.readline
N = int(input())
que = []
for i in range(N):
    nums = list(map(int, input().split()))
    if que:
        for num in nums:
            if que[0] < num:
                heapq.heappush(que, num)
                heapq.heappop(que)
    else:
        
        for num in nums:
            heapq.heappush(que, num)


print(que[0])
