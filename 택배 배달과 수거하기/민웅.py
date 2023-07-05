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