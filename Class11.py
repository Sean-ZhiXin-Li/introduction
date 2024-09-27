n = 6
fish = [4, 3, 0, 5, 1, 2]
for i in range(0, 6):
    numbers = 0
    for j in range(0, i):
        if fish[i] - fish[j] > 0:
            numbers = numbers + 1
    print(numbers)
