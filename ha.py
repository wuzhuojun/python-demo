print('输出中文')

print(100 + 200)

a = 100
print(a)

print('123%d%s' % (1, 1))

people = ['joven', 'shawn', 'paker']
print(len(people))

print(people[1])

a_sum = 0
for x in [1, 2, 3]:
    a_sum = a_sum + x

print(a_sum)


def num_sum():
    f_sum = 0
    for x in [1, 2, 3]:
        f_sum = f_sum + x
    return f_sum


sum2 = num_sum()

print(sum2)


def add(a, b):
    return a + b


print(add(1, 2))

L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2

print(L)

