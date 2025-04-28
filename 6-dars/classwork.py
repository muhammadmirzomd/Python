# 14

# 1 2 3 = =  3 1 2
# 300
# 20
# 2
# son = 123
# y = son // 100  # 1
# o = (son // 10) % 10 # 2
# d = son % 10 # 3
# n = d * 100 + y * 10 + o
# print(n)


# 1234 1
# son = 1234
# a = son // 100 # 12
# n = a % 10
# print(n)

sekunt = int(input("S = "))
soat = sekunt // 3600
minut = (sekunt % 3600) // 60
sekunt = sekunt % 60
print(f"{soat}:{minut}:{sekunt}")
