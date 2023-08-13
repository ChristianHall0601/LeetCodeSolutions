class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNegative = False
        if x < 0:
            isNegative = True
            x = x*(-1)
        stringX = str(x)
        stringX = stringX[::-1]
        answer = int(stringX)
        if answer >= ((2**31)-1):
            answer = 0
        elif answer <= ((2**31)*-1):
            answer = 0
        if isNegative:
            answer = answer*(-1)
        return answer
