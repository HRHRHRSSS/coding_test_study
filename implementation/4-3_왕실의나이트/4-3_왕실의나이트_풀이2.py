import sys
from io import StringIO
test_input = """c2"""
sys.stdin = StringIO(test_input)
############################################
x,y = sys.stdin.readline().strip()

# x를 아스키 값으로 변환하여 숫자로 변환
# a의 아스키 코드 +1 (좌표는 1부터 시작이니까)
x = ord(x) - ord('a') + 1
y = int(y)

# 나이트가 이동할 수 있는 8가지 방향 정의
moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), 
         (2, 1), (1, 2), (-1, 2), (-2, 1)]

cnt = 0

# 각 방향으로 이동이 가능한지 확인
for move in moves:
    nx = x + move[0]
    ny = y + move[1]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        cnt += 1

print(cnt)