class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        else:
            listString = []
            goDown = True
            for i in range(numRows):
                listString.append("")
            i = 0
            k = 0
            while i < len(s):
                if k== numRows-1:
                    goDown = False
                if k==0:
                    goDown = True
                listString[k] = listString[k] + s[i]
                if goDown:
                    k = k+1
                else:
                    k = k-1
                i = i +1
            myResult = ""
            for i in range(len(listString)):
                myResult = myResult + listString[i]
            return myResult
