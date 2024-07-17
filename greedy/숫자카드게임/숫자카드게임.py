#테스트용 입력 예제
#test_input = """3 3
#3 1 2
#4 1 4
#2 2 2"""

test_input = """2 4
7 3 1 8
3 3 3 4"""

import sys
from io import StringIO

# 테스트용 입력을 표준 입력으로 설정
sys.stdin = StringIO(test_input)
#----------------------------------------------
N,M = map(int,sys.stdin.readline().split())
arr = [] #행마다 min값 저장할 리스트

for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    arr.append(min(lst))

print(max(arr))