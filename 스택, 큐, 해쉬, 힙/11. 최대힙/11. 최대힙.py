# 부모가 자식노드보다 항상커야함
# 그냥 heap 쓰면 최소힙으로 작동 된다.

# 그래서 최대힙을 만들고 싶으면 부호를 바꿔서 하면된다.
import heapq as hq
a = [] # heapq 를 import 하면 빈리스트가 힙 처럼 조작이 가능
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(-(hq.heappop(a))) # heappop 하면 루트 노드값 출력 그리고 가장 밑에 있고 오른쪽의 자료가 루트노드로 감
    else:
        hq.heappush(a,-n) # heappush  최소힙의 형태로 푸쉬 a에다 n값을 넣어라