#테스트용 입력 예제
test_input = """5 3
1 2 5 4 3
5 5 6 6 5
"""
import sys
from io import StringIO
# 테스트용 입력을 표준 입력으로 설정
sys.stdin = StringIO(test_input)
#------------------------------------------------
n, k = map(int, sys.stdin.readline().split())

# 배열 A,B 입력받기
arrA = list(map(int,sys.stdin.readline().split()))
arrB = list(map(int,sys.stdin.readline().split()))

# A배열은 오름차순, B배열은 내림차순으로 정렬
arrA = sorted(arrA)
arrB = sorted(arrB, reverse=True)

# k번만큼 순회하며 원소 변경
for i in range(k):
    arrA[i], arrB[i] = arrB[i], arrA[i]

# A배열 원소의 합 출력
print(sum(arrA))