import math

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.dist((x1, y1), (x2, y2))  # 두 터렛 사이 거리

    # 두 원이 같은 경우 (중심도 같고 반지름도 같음)
    if d == 0 and r1 == r2:
        print(-1)
    # 두 원이 만나지 않는 경우
    elif d > r1 + r2 or d < abs(r1 - r2):
        print(0)
    # 외접 or 내접 (한 점에서 만남)
    elif d == r1 + r2 or d == abs(r1 - r2):
        print(1)
    # 두 점에서 만나는 경우
    else:
        print(2)
