# 재귀적으로 구현한 n!
def factorial(n):
    # 기저 사례: n이 0인 경우
    if n == 0:
        return 1
    else:
        # 재귀 호출 : n * (n-1)!
        return n * factorial(n-1)
    
# 코드 설명
# 1. 'factorial(n)' 함수가 호출되면 먼저 n이 0인지 확인/ 0이면 기저 사례로 1반환
# 2. 0이 아니라면, 'n * factorial(n-1)' 계산
# 이때, factorial(n-1) 이 재귀호출 통해 다시 n-2, n-3 호출로 이어짐
# 3. 모든 재귀호출이 기저 사례에 도달하면 계산이 완료되고 결과 반환!

#---------------------------------------------------
# 예시!
# factorial(5)를 호출
# factorial(5)는 5 * factorial(4)을 반환합니다.
# factorial(4)는 4 * factorial(3)을 반환합니다.
# factorial(3)는 3 * factorial(2)을 반환합니다.
# factorial(2)는 2 * factorial(1)을 반환합니다.
# factorial(1)는 1 * factorial(0)을 반환합니다.
# factorial(0)는 1을 반환합니다.