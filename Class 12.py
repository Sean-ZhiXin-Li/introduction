
# n = 6
# fish = [4, 3, 0, 5, 1, 2]
# MAX = fish[0]
# for i in range(0,6):
#         if MAX - fish[i] < 0:
#             MAX = fish[i]
# print(MAX)

# n = 6
# fish = [4, 3, 0, 5, 1, 2]
# target = -10
# hasfactor = 0
# for i in range(0,6):
#     if target - fish[i] == 0:
#         hasfactor = 1
# if hasfactor == 0:
#     print("NO")
# else:
#     print("YES")


n = 6
fish = [4, 3, 0, 5, 1, 2]
target = -10
exist = False
for i in range(0,6):
    for j in range(i+1,n):
        if fish[i]+fish[j]==target:
            exist = True
if exist == False:
    print("NO")
else:
    print("YES")

