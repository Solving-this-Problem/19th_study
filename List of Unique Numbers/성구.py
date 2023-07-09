# 1205 등수구하기
import sys
input = sys.stdin.readline
'''
0 <= N =< P
10 <= P <= 50
0 <= 점수 <= 2,000,000,000
현재 랭킹 리스트 점수가 비오름차순(내림차순)으로 주어진다.
'''       

N, newScore, P = map(int, input().strip().split())
if not P:       # 랭킹 갯수 0개
    print(-1)
elif not N:     # 리스트 갯수 0개
    print(1)
else:   
    RankList = list(map(int, input().strip().split()))
    if RankList[N-1] > newScore:    # 최솟값이 새로운 값보다 클때
        if N == P:                  # 리스트가 다 차있을 때는 들어갈 수 없음
            print(-1)
        else:
            print(N+1)
    
    elif RankList[N-1] == newScore and N==P:    # 리스트가 다 차있는데 최솟값과 새로운값이 같아도 들어갈 수 없음
        print(-1)
    else:   # 그 외엔 내가 가질 수 있는 최대 등수로 들어가기
        ans = -1
        for i in range(N):
            if RankList[i] <= newScore:
                ans = i+1
                break
        print(ans)