#숫자 사이에 +, * 를 삽입하여 가장 큰 수 만들기
inp = input()
lis = list(map(int, inp)) # int형으로 저장
#print(type(lis[1]))
res = lis[0]
for i in lis[1: ]:
    # if res + i > res * i:
    #     res += i
    # else:
    #     res *= i
    if i < 2:
        res += i
    else:
        res *= i 
print(res)