# int, float
# a = 1
# b = 1.0

# print
# print(a, type(a))
# print(b, type(b))

# bool
# c = True
# d = False
# print(c, type(c))
# print(d, type(d))

# str
# e = "Sample'''''' text"
# e_1 = 'Sample""""" text'
# print(e, e_1)


# list tuple set dict
# l = [1, 2, 3, 4]
# t = (1, 2, 3, 4)
# s = {1, 2, 3, 4}
# d = {1: "orange",
#      2: "apple",
#      3: "pineapple"}


# print(s[2])  # выдаст ошибку
# print(d[1], d[2], d[3])
# print(d[0])

# l.append(123123)
# print(l)
# s.add(1123123123)
# print(s)

# d[10] = l
# print(d)

# d_1 = {
#     1: {
#         "name": "orange",
#         "manufacturer": "Romashka"
#     },
#     2: {
#         "name": "orange",
#         "manufacturer": "Solnyshko"
#     },
#     3: {
#         "name": "pineapple",
#         "manufacturer": "Zvezda"
#     }
# }
#
# print(d_1[3]["manufacturer"])


# if

# a = 1
#
# if a == 1:
#     print("a is equal 1")
# elif a > 1:
#     print("a is greater than 1")
# else:
#     print("a is not greater than 1")

# while
cnt = 0
# print(cnt == 10)

while cnt <= 10:
    print("cnt is:", cnt)
    cnt = cnt + 1
