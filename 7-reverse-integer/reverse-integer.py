class Solution:
    def reverse(self, x:int):
        MAX=2**31
        MIN=-MAX
        num = x
        rev = 0
        negative = False
        
        if num < 0:
            negative = True
            num = -num
        
        while num > 0:
            k =num %10
            rev =rev *10 + k
            num =num //10
        
        if negative:
            rev = -rev
        
        
        
        return rev if MIN<=rev<= MAX else 0