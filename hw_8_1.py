data = [i ** 2 for i in range(0, 20)]
print(data)

data1 = [i % 3 for i in data]
print(data1)


data2 = [1, 'd', 3, 'g', 'qwe', 2342, 0]
data3 = [item for item in data2 if type(item) == int]
print(data3)




