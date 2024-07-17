#테스트용 입력 예제
test_input = """17 4"""
import sys
from io import StringIO
import math
# 테스트용 입력을 표준 입력으로 설정
sys.stdin = StringIO(test_input)
#----------------------------------------
N,K = map(int,sys.stdin.readline().split())

cnt = 0
n1 = N % K # 나눠지지않으면 그 만큼 빼주기
N = N - n1

# 나눠지게 만들어놓고!
# 거듭제곱을 구해서 얼마나 나누면 1이 되는지 구하기
n2 = int(math.log(N, K))

# 과정 수행 횟수
cnt = n1+ n2
print(cnt)