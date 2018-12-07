# -*- coding: utf-8 -*-
# @Time     : 2018/12/7 22:14
# @Author   : Junee
# @FileName: 循环体中的条件控制.py
# @Software  : PyCharm
# Observing PEP 8 coding style

# 测试for循环的i 在循环体内部是否可以修改
for i in range(10):
    if i == 5:
        i += 1
    print(i)

def numberOfLines(widths, S):
    """
    :type widths: List[int]
    :type S: str
    :rtype: List[int]
    """
    index = [ ]
    if S == '':
        return 0, 0
    for each in S:
        index.append(ord(each) - 97)
    sum = 0
    row = 1
    # for i in range(len(index)):
    #     sum += widths[ index[ i ] ]
    #     print(i,sum)
    #     if sum >= 100:
    #         sum = 0
    #         row += 1
    #         i -= 1  # 新手错误，在for i 循环内部修改i，里面的i可以改变，但是改不了循环条件中的i
    #         # 这种情况下，应该将for循环改成While循环，如下
    i = 0
    while i < len(index):
        sum += widths[index[i]]
        print(i,sum)
        if sum > 100:
            sum = 0
            row += 1
            i -= 1
        if sum == 100:  # 之前把>=100写在一起，这是不对的，当=100时，并不需要原地踏步，否则就多算了一次，
            # 如下，=100跟>100差了一步
            sum = 0
            row += 1
        # else:
        #     i += 1
        # 新手常见错误，误以为上面的减一是回退，其实不是，应该是原地踏步
        # 如果把i ++ 写在else里，会导致回退到溢出之前的那一位导致错误，因为上一位并没有溢出
        # 我们要的是原地踏步，所以应该在最后对每一次都自增
        i += 1

    return row, sum
