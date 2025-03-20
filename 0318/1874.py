import sys

number = int(sys.stdin.readline().strip())
if ( 1 > number or number > 100000):
    sys.exit()
list = []
purpose = [] # 목표 결과 담을 배열
stack = []
result = []

for i in range(number):
    list.append(i+1)

purpose = [int(sys.stdin.readline().strip()) for _ in range(number)]

# print(purpose)
# print(len(list))

i = 0
z = 0
while( z < number):
    if(list[0] <= purpose[i]):
        while(z < len(list) and list[z] <= purpose[i]):
            stack.append(list[z])
            # print('append on stack ' + str(list[z]))
            z += 1
            result.append('+')
            # if (z == number):
            #     for k in range(len(stack)):
            #         top = stack.pop()
            #         if (top < purpose[i]):
            #             print('No')
            #             quit()
            #         print('stack poped')
            #         result.append('-')
            #     break
            if z == number:
                while stack:
                    top = stack.pop()
                    result.append('-')  # "-"
                break
        i += 1
        if stack:
            stack.pop()
            # print('stack poped')
            result.append('-')
    else:
        # stack 안에 있을 경우
        # for j in range(len(stack)):
        #     if stack[j] == purpose[i]:
        #         index = j
        #         i += 1                       
        #         for j in range(len(stack) - index):
        #             stack.pop()
        #             print("top : " + str(top))
        #             print('stack poped')
        #             result.append('-')
        #         break
        # stack 안에 있을 경우
        if not stack or stack[-1] != purpose[i]:  # ✅ pop할 값이 다르면 NO
            # print('NO')
            sys.exit()
        stack.pop()
        result.append('-')  # "-"
        i += 1

sys.stdout.write("\n".join(result) + "\n")