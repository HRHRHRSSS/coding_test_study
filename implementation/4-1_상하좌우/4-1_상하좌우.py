#테스트용 입력 예제
test_input = """5
R R R U D D"""

import sys
from io import StringIO

# 테스트용 입력을 표준 입력으로 설정
sys.stdin = StringIO(test_input)
#------------------------------------------
N = int(sys.stdin.readline()) # 공간의 크기
arr = list(sys.stdin.readline().split()) # 이동 계획서

x=1
y=1

for i in arr:
    if (i=='R') & (y!=N):
        y += 1
    elif (i=='L') & (y!=1):
        y -= 1
    elif (i=='D') & (x!=N):
        x += 1
    elif (i=='U') & (x!=1):
        x -= 1
    else:
        pass

# 숫자 공백 포함 출력 방법!!!
print(x, y) # 쉼표로 구분
print(f'{x} {y}') # f-string 사용
print('{} {}'.format(x, y)) # 문자열 포맷팅 사용
print(str(x)+ ' ' +str(y)) # 문자열 연결 연산자 사용

