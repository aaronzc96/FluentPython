import array
import os
import dis
from collections import namedtuple

symbols = '$¢£¥€¤'

# 列表推导list comprehension(listcomps) 唯一作用：生成列表
codes = [ord(symbol) for symbol in symbols]
print(codes)

x = 'ABC'
dummy = [ord(x) for x in x]
print(dummy, x)

# map/filter
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(x, y) for y in sizes for x in colors]
print(tshirts)

# 生成器表达式将列表推导的[]改为()
# 生成器不会产生一个6个元素的列表，而是在运行过程中一个一个产生，所以开销小
print(tuple(ord(symbol) for symbol in symbols))
print(array.array('I', (ord(symbol) for symbol in symbols)))
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

# 元组拆包
# 用*把可迭代对象拆包赋给一个函数的参数
t = (20, 8)
print(divmod(*t))
# os.path.split返回的元组，拆分为路径和文件名
_, filename = os.path.split('/1/2/3/4/t.txt')
print(filename)
# 用*处理剩余元素，用*arg来获取不确定数量的参数
# *只能使用在一个变量名前面，可以放在任何位置
a, b, *rest = range(5)
a1, *rest1, b1 = range(5)
print(a, b, rest, a1, rest1, b1)
# 嵌套拆包
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    # 西半球
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))

# 具名元组（和类很像）
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo.population)
# 具名元组的属性和方法
# 1. _fields 包含元组元素名的列表
# 2. _make 用可迭代对象生成元组
# 3. _asdict 把具名元组以collections.OrderedDict形式返回
print(City._fields)
LatLong = namedtuple('LatLong', 'Lat Long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
for key, value in delhi._asdict().items():
    print(key + ':', value)

# P32解释很优秀
# 列表组成的列表
# 正确
board = [['_'] * 3 for i in range(3)]
board[1][2] = 'X'
print(board)
# 错误
board = [['_'] * 3] * 3
board[1][2] = 'X'
print(board)

# += *= 作用在可变与不可变序列上结果差别：可变原地加法 不可变地址改变
a = [1, 2, 3]
b = [1, 3, 4]
c = (1, 2, 4)
d = (2, 4, 5)
print(id(a), id(c))
a += b
c += d
print(id(a), id(c))

dis.dis('s[a] += b')

