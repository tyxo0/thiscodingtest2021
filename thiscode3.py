#공포도가 n인 모험가는 n명 이상의 모험가랑 팀
#모든 모험가를 쓸 필요는 없음
from collections import Counter

n = (int)(input())
inp = list(map(int, input().split()))
sinp = sorted(inp) # 오름차순 정렬
cnt = 0 # 팀 수

#같은 공포도의 모험가 수 활용
fearType = list() #공포도 종류 저장
typeNum = list() #같은 공포도 모험가 수 저장

ftemp = sinp[0]
fearType.append(sinp[0])
for i in sinp:
    if(i != ftemp):
        fearType.append(i)
        ftemp = i

#같은 공포도끼리 팀구성하고 남은 인원들로 다시 팀 구성
cnter =Counter(sinp)
#같은 공포도끼리 팀구성
for i in fearType:
    temp = cnter[i] #같은 공포도의 모험가 수
    
    if(temp >= i): #같은 공포도로 팀구성 가능
        cnt += temp // i
        temp -= temp // i * i #팀에 들어간 모험가 제외 후 남은 모험가 저장
        typeNum.append(temp)
    else:
        typeNum.append(temp)

#남은 인원들로 다시 팀 구성
rtemp = 0 
for i in range(0, n):
    rtemp += typeNum[i]
    if(rtemp >= fearType[i]):
        rtemp -= fearType[i]
        cnt += 1

print(cnt, fearType, typeNum)



