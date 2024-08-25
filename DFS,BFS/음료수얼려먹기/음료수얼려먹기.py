# 테스트 케이스
n, m = 4, 5
graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

# N, M을 공백을 기준으로 구분하여 입력받음
#n, m = map(int,input().split())

# 2차원 리스트 맵 정보 입력받기
#graph = []
#for i in range(n):
#    graph.append(list(map(int,input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들 방문
def dfs(x,y):
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x<0 or y>m-1 or y<0 or x>n-1:
        return False
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x+1,y) # 상,하,좌,우에 대해 dfs 함수 호출
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x,y-1)
        return True
    return False

# dfs를 호출
count = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count += 1
print(count)