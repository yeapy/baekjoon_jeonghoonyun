import sys

number = int(sys.stdin.readline().strip())

# ✅ 입력값 범위 체크 (논리 OR 사용)
if number < 1 or number > 100000:
    sys.exit()

stack = []
result = []
current = 1  # ✅ 1부터 시작하는 오름차순 숫자

purpose = [int(sys.stdin.readline().strip()) for _ in range(number)]  # ✅ 빠른 입력

for target in purpose:
    while current <= target:  # ✅ target까지 push
        stack.append(current)
        result.append('+')
        current += 1  # ✅ 숫자 증가 (list 사용하지 않음)

    if stack and stack[-1] == target:  # ✅ pop할 수 있는 경우
        stack.pop()
        result.append('-')
    else:  # ✅ pop할 수 없는 경우 → "NO"
        print("NO")
        sys.exit()

sys.stdout.write("\n".join(result) + "\n")  # ✅ 빠른 출력
