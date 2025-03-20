N = int(input())
size = list(map(int, input().split())) #입력 : 1 2 3 /출력 : [1, 2, 3] 
T, P = map(int, input().split())


sum = 0

for i in range(6):
    if size[i] % T == 0:
        sum = sum + (size[i] // T)
    else:
        sum = sum + (size[i] // T) + 1
result = N // P
left = N % P

print(sum)
print(str(result) + " " + str(left))

