n, k = map(int, input().split())
cnt =0

## n=100000, k = 7777인 경우 리소스를 많이 씀
# while n != 1:
#     if n % k == 0:
#         n //= k
#         cnt += 1
#     else: 
#         n -= 1
#         cnt += 1
# print(cnt)
# 5  ## tar = 3
while True: # 25 3  24  1  n=8  cnt = 2 
    # tar=6 cnt = 4 2 5  
    target = (n//k) * k # n이 k로 나누어 떨어지는 가장 큰 값 구하기 
    cnt += n-target  # n-target만큼 빼주어야 나눌 수 있음. 
    n = target # n에 나눈 나머지 할당 
    #n을 어떻게든 나누어 줄 수 있게 만듦
    if n < k: #탈출 조건 위치를 어디에 두어야 하는가? 
        cnt += n-1
        break
    n //= k # n>k일 경우 나눠줄 필요가 없으므로 탈출조건을 위에 쓴다.
    cnt += 1
    ## 나머지를 다시 나눠줘야 함 
    # if n < k: 
    #     cnt += n-1
    #     break
print(cnt) #