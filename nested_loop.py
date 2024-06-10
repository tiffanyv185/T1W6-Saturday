# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # # print(matrix[1][1])


# for rows in matrix:
#     for item in rows:
#         if item == rows[1]:
#             print(item, end =" ")
#     print()

stars = 5

# *
# **
# ***
# ****
# *****

for i in range (1, stars + 1):
    for j in range(i):
        print("*", end = "")
    print()

