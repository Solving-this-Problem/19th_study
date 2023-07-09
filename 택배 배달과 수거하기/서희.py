# include <stdio.h>
# include <stdbool.h>
# include <stdlib.h>

# deliveries_len은 배열 deliveries의 길이입니다.
# pickups_len은 배열 pickups의 길이입니다.
def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver_stack, pickup_stack = [], []
    for i in range(n):
        if deliveries[i] != 0:
            deliver_stack.append(i)
        if pickups[i] != 0:
            pickup_stack.append(i)
    while deliver_stack or pickup_stack:
        C = cap
        if len(deliver_stack) == 0 and len(pickup_stack) != 0:
            answer += (pickup_stack[-1] + 1) * 2
        elif len(deliver_stack) != 0 and len(pickup_stack) == 0:
            answer += (deliver_stack[-1] + 1) * 2
        elif deliver_stack[-1] >= pickup_stack[-1]:
            answer += (deliver_stack[-1] + 1) * 2
        else:
            answer += (pickup_stack[-1] + 1) * 2
        while deliver_stack and C != 0:
            index = deliver_stack.pop()
            if deliveries[index] <= C:
                C -= deliveries[index]
                deliveries[index] = 0
            else:
                deliveries[index] -= C
                C = 0
                deliver_stack.append(index)
        # 돌아올때 택배를 수거하기 위해 택배차의 공간 초기화
        C = cap - C
        while pickup_stack and C != 0:
            index = pickup_stack.pop()
            if pickups[index] <= C:
                C -= pickups[index]
                pickups[index] = 0
            else:
                pickups[index] -= C
                C = 0
                pickup_stack.append(index)
    return answer
