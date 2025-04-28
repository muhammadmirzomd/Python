# 1-misol
n = int(input("n: "))
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)

# 2-misol
n = int(input("n: "))
for i in range(1, n + 1):
    if i % 3 == 0:
        print(i)
    if i % 5 == 0:
        print(i)
    if i % 7 == 0:
        print(i)

# 3-misol
n = int(input("n: "))
for i in range(2, n + 1):
    tub = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            tub = False
            break
    if tub:
        print(i)

# 4-misol
n = int(input("n: "))
for i in range(n, 0, -1):
    if i % 5 == 0:
        print(i)

# 5-misol
n = int(input("n: "))
c = 0
for i in range(1, n + 1):
    if i % 2 == 0 and i % 3 == 0:
        c += 1
print(c)

# 6-misol
n = int(input("n: "))
s = 0
for i in range(1, n + 1):
    if i % 2 == 1:
        s += i
print(s)

# 7-misol
n = int(input("n: "))
for i in range(1, n + 1):
    if i % 4 == 0 and i % 8 != 0:
        print(i)

# 8-misol
n = int(input("n: "))
i = 1
while i <= n:
    if i > 0:
        print(i ** 2)
    i += 1

# 9-misol
while True:
    x = int(input("son: "))
    if x == 0:
        break
    if x > 0:
        print("musbat")
    elif x < 0:
        print("manfiy")
    else:
        print("0")

# 11-misol
a = int(input("a: "))
b = int(input("b: "))
for i in range(b, a - 1, -1):
    print(i)

# 12-misol
n = int(input("n: "))
for i in range(1, n + 1):
    if i % 5 == 0 and i % 3 != 0:
        print(i)

# 13-misol
s = 0
while True:
    x = int(input("son: "))
    if x == -1:
        break
    if x > 0:
        s += x
print(s)

# 14-misol
n = int(input("n: "))
yig = 0
while n > 0:
    yig += n % 10
    n //= 10
print(yig)

# 15-misol
n = int(input("n: "))
kop = 1
for i in range(1, n + 1):
    if i % 2 == 0 and i % 3 == 0:
        kop *= i
print(kop)

# 19-misol
count = 0
while True:
    x = int(input("son: "))
    if x == 0:
        break
    if x % 2 == 1 and x > 0:
        count += 1
print(count)


"""
10-misol
16-misol
17-misol
18-misol
20-misol
"""