import sys
from io import StringIO
# 1 : N x M 맵 크기
# 2 : (A,B) (방향)
test_input = """4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1"""
sys.stdin = StringIO(test_input)
############################################
N, M = map(int,sys.stdin.readline().split())
# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * M for _ in range(N)]
# 현재 캐릭터의 x좌표, y좌표, 방향
x, y, direction = map(int, sys.stdin.readline().split())
# 0은 땅, 1은 바다 / 방문한 곳도 1로 처리
# 현재 좌표 1로 처리
d[x][y] = 1

# 전체 맵 정보 입력받기 (육지/바다)
arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))


# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전 ( = d가 -1 되는 것과 같음)
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0

while True:
    # 왼쪽으로 회전하기
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    # 땅이여야 하고 + 가보지 않은 칸이여야 함
    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1 # 이제 가본걸로
        x = nx
        y = ny
        count += 1 # 가본 칸 수
        turn_time = 0
        continue
    # 바다이거나 + 다 방문한 곳인 경우
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우 (후진)
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        #뒤로 갈 수 있는지 확인(땅인지)
        if arr[nx][ny] == 0:
                x = nx
                y = ny
        
        # 뒤가 땅이 아니라 바다라면?
        else:
             break
        turn_time = 0

print(count)