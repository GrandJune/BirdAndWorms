# -*- coding: utf-8 -*-
# @Time     : 2018/12/11 11:15
# @Author   : Junee
# @FileName: x的平方根.py
# @Software  : PyCharm
# Observing PEP 8 coding style

# 递归法写二分查找没法返回值：原问题代码
# def half_search(s, e,nums, target):
#     if s > e:
#         return -1
#     h = (s + e) // 2
#     print(s,h,e)
#     if nums[h] == target:
#         print("find!!!")
#         return '返回值测试' # 这里的return都没有返回值，原因，这个是返回成下面条件语句里头的递归函数的返回值，
#         # 但是那个递归函数没有采用返回值，导致了这个返回值凭空蒸发了
#     elif nums[h] > target:
#         half_search(s + 1, h, nums,target)
#         print("左半边")
#         return h # 这里头的h 永远是第一次的h，因为在迭代里面修改的h没有反映出来,应该加一个返回值
#         # 迭代里面的h是被修改了，但是我们这个return是在迭代子函数之外的，反应的总是最外层的h
#     elif nums[h] < target:
#         half_search(h + 1, e, nums,target)
#         print('右半边')
#         return h

# 结论，应该要给递归子函数加一个返回值，用来反映到上层，才能对上层的参数进行更新
def half_search(s, e,nums, target):
    if s > e:
        return -1
    h = (s + e) // 2
    print(s,h,e)
    if nums[h] == target:
        print("find!!!",h)
        return h
    elif nums[h] > target:
        h = half_search(s + 1, h, nums,target)
        print("左半边")
        return h # 这里头的h 永远是第一次的h，因为在迭代里面修改的h没有反映出来,应该加一个返回值

    elif nums[h] < target:
        h = half_search(h + 1, e, nums,target)
        print('右半边')
        return h
    return h

nums = [-1,0,3,5,9,12,13,14,15,16,17,18,19]
target = 18
# nums = [-1,0,3,5,9,12]
# target = 2
s, e = 0,len(nums)-1
<<<<<<< HEAD
re = half_search(s,e,nums,target)
=======
re = half_search(s,e,nums,target)  # 写递归时，明明已经找到了解，却无法return，莫名其妙的错误
>>>>>>> origin/master
print(re)
