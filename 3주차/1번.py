# 버블정렬 방식
print("길이")
N = int(input())

print("배열")
numbers = []

for _ in range(N) : 
    numbers.append(int(input()))
    
print("결과")
# Bubble Sort
for i in range(len(numbers)) : 
    for j in range(len(numbers)) : 
        if numbers[i] < numbers[j] : 
            numbers[i], numbers[j] = numbers[j], numbers[i]
            
for n in numbers : 
    print(n) 