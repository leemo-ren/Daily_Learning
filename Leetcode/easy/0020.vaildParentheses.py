'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''
#%%
#
#根据ASII码的大小顺序来排列
#   (   40
#   )   41
#   {   123
#   }   125
#   [   91
#   ]   93

c1 = "()"       #00
c2 = "()[]{}"   #001122
c3 = "(]"       #02
c4 = "([)]"     #0202
c5 = "{[]}"     #1221

dic = {'(':0,')':0,'{':1,'}':1,'[':2,']':2}


def vaild(c):
    j = 0 
    i = 0
    value = 0
    while( i < len(c)):
        if c[i] in dic:
            value = dic[c[i]]
            j = i
        i = i + 1
        if i<len(c) and i == j+1:
            if value == dic[c[i]]:
                c = c.strip(c[i-1])
                c = c.strip(c[i-1])
                i=0
                continue
        if i == len(c):
            break
    if len(c) == 0:
        return True
    else: 
        return False

if __name__ == "__main__":
    print(vaild(c1))
    print(vaild(c2))
    print(vaild(c3))
    print(vaild(c4))
    #print(vaild(c5))
    print('----------')


# %%
def vaildParenttheses(c):
    dict0 = {'(':')','{':'}','[':']'}
    stack = []
    for i in range(len(c)):
        #遇到左半符号时，将其对应的右半符压入栈中
        if c[i] in dict0:
            stack.append(dict0[c[i]])
        #遇到右半符号，从栈中读取第一个字符，判断是否相等
        else:
            if stack.pop() != c[i]:
                return False
    if len(stack)==0:
        return True

if __name__ == "__main__":
    print(vaildParenttheses(c1))
    print(vaildParenttheses(c2))
    print(vaildParenttheses(c3))
    print(vaildParenttheses(c4))
    print(vaildParenttheses(c5))



