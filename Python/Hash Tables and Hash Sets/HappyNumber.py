class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        answerHash = set()
        answerHash.add(n)
        
        numberList = [int(i) for i in str(n)]
        
        while numberList != [1]:
            total = 0
            for number in numberList:
                total += number*number
            
            #check if answer appeared previously
            if total in answerHash:
                return False
            else:
                answerHash.add(total)
            
            numberList = [int(i) for i in str(total)]
            
        return True