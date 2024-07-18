import sys
from io import StringIO
test_input = """c2"""
sys.stdin = StringIO(test_input)
############################################
x,y = sys.stdin.readline().strip()

# 문자를 숫자로 변환
map1 = {'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8}

# x와 y를 정수로 변환
x = map1[x]
y = int(y)

cnt = 0
# 수직 2칸(상하)로 이동이 가능한가? (y좌표 관련)
# up
if y-2 > 0:
    if (x-1) > 0:
        cnt+=1
    if (x+1) < 9:
        cnt+=1
# down
if (y+2) < 9:
    if (x-1) > 0:
        cnt+=1
    if (x+1) < 9:
        cnt+=1
# 수평 2칸(좌우)로 이동이 가능한가? (x좌표 관련)
# left
if (x-2) > 0:
    if (y-1) > 0:
        cnt+=1
    if (y+1) < 9:
        cnt+=1
# right
if (x+2) < 9:
    if (y-1) > 0:
        cnt+=1
    if (y+1) < 9:
        cnt+=1

print(cnt)