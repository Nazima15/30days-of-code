import sys

T = int(sys.stdin.readline())
count0 = [0] * 41
count1 = [0] * 41

# 초기값 설정
count0[0], count1[0] = 1, 0
count0[1], count1[1] = 0, 1

# DP 테이블 채우기
for i in range(2, 41):
    count0[i] = count0[i-1] + count0[i-2]
    count1[i] = count1[i-1] + count1[i-2]

# 테스트케이스 출력
for _ in range(T):
    n = int(sys.stdin.readline())
    print(count0[n], count1[n])
