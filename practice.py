# 12:00 시작 12: 42분 마침 못품
# 일단 개장부터 맨앞 놀이기구 시작시간과 맨뒤 놀이기구 마감시간부터 마감까지는 무조건 시간이 나옴 ㅇㅇ 그래서 둘중 비교해서 더 큰애를 largest에 넣기로함
# 그리고 끝나는 순서로 정리를 해서 겹치는지 안겹치는지 확인 겹친다면 시간이 안남고 
# 안겹친다면 시간이 남을거임.. 예제코드 기준으로 3타임이니까 1) 시작 2) 끝 3) 중간중간 2개 그치만 겹칠수도 있슴
# 다른건 괜찮은 것 같은데 저 숫자들이 더한다고 빼진다고 시간으로 안나온다는게 ( 60진법으로 변환을 못하겠다...)
# 1000  
n = int(input())
time = []
for _ in range(n):
    s, e = map(int,input().split())
    s = (s//100)*60 + (s%100)
    s = (s//100)*60 + (s%100)
    time.append((s,e))
time.sort()
f1 = time[0][0] -10 - 600 # 무조건 첫 쉬는 시간
time.sort(key = lambda x : (x[1],x[0]))
f2 = (2200//100)*60 - (time[n-1][1]+10)
largest = max(f1,f2)
et = 0 # 놀이기구 끝나는 시간

for s, e in time:
    if s-10 > et+10:
        if largest < (s-10)-(et+10):
            largest = (s-10)-(et+10)
    et = e
print(largest)
    

