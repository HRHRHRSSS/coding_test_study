#테스트용 입력 예제
test_input = """5 8 3
2 4 5 4 6"""

import sys
from io import StringIO

# 테스트용 입력을 표준 입력으로 설정
sys.stdin = StringIO(test_input)

#----------------------------------------------------
# N,M,K 대입하기
N,M,K = map(int,sys.stdin.readline().split())
# 두 번째 줄 list 입력받기
arr = list(map(int, sys.stdin.readline().split()))

# list 정렬하기
arr.sort()

# 가장 큰 수
max = arr[N-1]
max2 = arr[N-2]

cnt = 0
# 가장 큰 수 더하기
n1 = M//3
cnt += max*(n1*K)

# 그 다음 큰 수도 더해주기
n2 = M%3
cnt += max2*n2

print(cnt)