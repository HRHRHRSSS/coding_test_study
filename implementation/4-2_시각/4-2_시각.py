import sys
from io import StringIO
test_input = """5"""
sys.stdin = StringIO(test_input)
############################################
# N 읽기
N = int(sys.stdin.readline())

count = 0
for t in range(N+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(t)+str(m)+str(s):
                count += 1

print(count)