'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''
import numpy as np

nums = [2,7,11,15]
target = 9

#%%
#常规操作

def TwoSum1(nums,target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j: #两者不为相同的数
                if nums[i] + nums[j] == target:
                    return i,j
        if i==len(nums) and j==len(nums):
            print("没有符合条件的数")
            return 0,0
    
if __name__ == "__main__":
    re1 = TwoSum1(nums,target)
    print(re1)

#总结：使用了两层for循环，时间复杂度O(n^2),空间复杂度O(1);


#%%
#改进：
# 增加一个 Map 记录已经遍历过的数字及其对应的索引值。
# 这样当遍历一个新数字的时候去 Map 里查询，target 与该数的差值是否已经在前面的数字中出现过。
# 如果出现过，那么已经得出答案，就不必再往下执行了。
# PS：python中的Map结构实际就是字典。

# def TwoSum(nums,target):
#     for i in range(len(nums)):

def TwoSum2(nums,target):
    dict0 = dict()
    for i in range(len(nums)):
        sub = target - nums[i]
        dict0[nums[i]] = i
        if sub in dict0:
            return dict0[sub],i    
    #return dict0.items() 可以查看字典中的数

if __name__ == "__main__":
    re2 = TwoSum2(nums,target)
    print(re2)

#总结：使用了一层for循环，时间复杂度O(n),空间复杂度O(n);
