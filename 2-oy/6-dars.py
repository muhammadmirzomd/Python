# fayl = open("namuna.txt", "a")
# fayl.write("\nSalom dunyo")
# fayl.close()
#
# a = open('namuna.txt', 'r')
# print(a.read())

# with open("namunaa.txt", 'x') as f:
#     a = f.write('Qalesa')
#     print(a)

with open('namunaa.txt', 'r')as f:
    for i in f.readlines():
        print(i.title())