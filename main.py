from collections import deque, defaultdict
from inspect import stack

class Solution(object):
    def func(self, main, sub):
        sub_string = ""
        if len(sub) == 0:
            return ""
        
        
        for i in main:
            pass
            
            
            
        return sub_string
        
        
    def get_dic(self, str):
        dic = {}
        for char in str:
            if char in dic:
                dic[char] +=1
            else:
                dic[char] = 1
        return dic
            
        
       
sol = Solution()
# print(sol.func("adobecodebanc", "abc"))
print(sol.get_dic("abbc"))