numbers = [1, 1, 3, 2, 1, 5, 3, 2]
count = 1
for i in range(0, 8):
    for j in range(i + 1, 8):
        if numbers[i] == numbers[j]:
            count += 1

numbers = [1, 1, 3, 2, 1, 5, 3, 2]
count = {}

for num in numbers:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

for num, freq in count.items():
    print(f"数字 {num} 出现了 {freq} 次")

numbers = [1, 1, 3, 2, 1, 5, 3, 2]
counted = []

for i in range(len(numbers)):
    if numbers[i] not in counted:
        count = 1
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                count += 1
        counted.append(numbers[i])
        print(f"数字 {numbers[i]} 出现了 {count} 次")

