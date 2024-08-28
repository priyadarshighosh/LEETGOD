
class Solution(object):
    def isPalindrome(self, x):
        num = x
        reversed_num = 0
        if x < 0:
            return False
        else:
            while num > 0:
                k = num % 10
                reversed_num = (reversed_num * 10) + k
                num = num // 10
            return reversed_num == x
