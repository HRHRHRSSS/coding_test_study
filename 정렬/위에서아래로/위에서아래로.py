#테스트용 입력 예제
test_input = """3
15
27
12"""
import sys
from io import StringIO
# 테스트용 입력을 표준 입력으로 설정
sys.stdin = StringIO(test_input)
#----------------------------------------------
n = int(sys.stdin.readline())

list = []
for i in range(n):
    list.append(int(sys.stdin.readline()))

# 오름차순 정렬
sorted_list = sorted(list, reverse=True)

# 정렬 수행 결과 출력
for i in sorted_list:
    print(i, end=' ') 
    
# end =' ' 
# : 는 파이썬의 print 함수에서 출력 뒤에 붙일 문자열을
# 지정하는 매개변수이다.
# 기본적으로 print 함수는 출력 후 자동으로 줄 바꿈('\n')을 추가
# 근데 end 매개변수를 사용하면 줄 바꿈 대신 다른 문자열 붙일 수 있음