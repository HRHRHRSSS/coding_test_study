#테스트용 입력 예제
test_input = """2
홍길동 95
이순신 77
"""
import sys
from io import StringIO
# 테스트용 입력을 표준 입력으로 설정
sys.stdin = StringIO(test_input)
#----------------------------
 # 학생 수
n = int(sys.stdin.readline())

# 모든 학생의 이름을 성적이 낮은 순서대로 출력
# 성적을 내림차순으로 정렬 - 출력은 학생 이름으로
arr = []
for i in range(n):
    input_data = sys.stdin.readline().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    arr.append((input_data[0], int(input_data[1])))

# 키(key)를 이용하여, 점수를 기준으로 정렬
# 각 튜플에서 성적(두 번째 요소)를 기준으로 정렬하겠다
sorted(arr, key=lambda student: student[1])

#정렬 수행 결과 출력
for student in arr:
    print(student[0], end=' ')