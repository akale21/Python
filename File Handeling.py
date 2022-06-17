
f = open('MyData.txt','r')
f1 = open("abc",'a')

f1.write(" interesting")

for data in f:
    f1.write(data)

# print(f.readline(), end='')
# print(f.readline())