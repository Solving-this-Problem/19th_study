# 리스트에 있는 점수 N
# 태수의 새로운 좀수
# 랭킹 리스트에 올라갈 수 있는 점수 갯수 P

N, num, P = map(int, input().split())


# print(type(num))
# print(type(lst[1]))

if N == 0:
    print(1)
elif N == P:
    K = 0
    scores = list(input().split())
    cnt = 1
    for score in scores:
        if int(score) > num:
            cnt += 1
        elif int(score) == num:
            if score == scores[N-1]:
                print(-1)
                K = 1
                break
            else:
                break
        else:
            break
    
    if not K:
        if cnt > P:
            print(-1)
        else:
            print(cnt)
else:
    scores = list(input().split())
    cnt = 1
    for score in scores:
        if int(score) > num:
            cnt += 1
        # elif int(score) == num:
        #     break
        else:
            break

    if cnt > P:
        print(-1)
    else:
        print(cnt)
