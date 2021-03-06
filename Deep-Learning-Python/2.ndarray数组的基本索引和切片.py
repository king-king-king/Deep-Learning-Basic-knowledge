import numpy

print('ndarray的基本索引')
x = numpy.array([[1, 2], [3, 4], [5, 6]])
print(x[0])  # [1,2]
print(x[0][1], x[2][1])  # 普通python数组的索引
print(x[0, 1], x[2, 1])  # ndarray数组的索引


x = numpy.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(x[0])  # [[1 2],[3 4]]
y = x[0].copy()  # 生成一个副本
z = x[0]  # 未生成一个副本
print(y)  # [[1 2],[3 4]]
print(y[0, 0])  # 1
y[0, 0] = 0
z[0, 0] = -1
print(y)  # [[0 2],[3 4]]
print(x[0])  # [[-1 2],[3 4]]
print(z)  # [[-1 2],[3 4]]

print('ndarray的切片1')
x = numpy.array([1, 2, 3, 4, 5])
print(x[1:3])  # [2,3] 右边开区间
print(x[:3])  # [1,2,3] 左边默认为 0
print(x[1:])  # [2,3,4,5] 右边默认为元素个数
print(x[0:4:1])  # [1,3] 下标递增2

print('ndarray的切片2')
x = numpy.array([[1, 2], [3, 4], [5, 6]])
print(x[:2])  # [[1 2],[3 4]]
print(x[:3, :1])  # [[1],[3]]
x[:2, :1] = 0  # 用标量赋值
print(x)  # [[0,2],[0,4],[5,6]]
x[:3, :1] = [[8], [6],[9]]  # 用数组赋值
print(x)  # [[8,2],[6,4],[5,6]]
