class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0] * len(temperatures)
        stack = []
        i=0
        
        for i,current in enumerate(temperatures):
            
            #go through stack
            while stack and current > temperatures[stack[-1]]:
                result[stack[-1]]= i-stack[-1]
                stack.pop()
            stack.append(i)

        return result
        """
        #1 pass, n solution
        result = []
        stack = []
        i=1
        
        while i < len(temperatures):
            
            current = temperatures[i]
            previous = temperatures[i-1]
            
            #go through stack
            while stack and current > temperatures[stack[-1]]:
                result[stack[-1]]= i-stack[-1]
                stack.pop()

            #compare w/ previous
            if current > previous:
                result.append(1)   
            else:
                result.append(0) #temp value
                stack.append(i-1)  
            
            i += 1
        
        result.append(0)
        return result
        """
        """
        #n^2 solution
        output = []
        i=0
        
        while i < len(temperatures)-1:
            counter = 0
            while (counter+i) < (len(temperatures)):
                if temperatures[i+counter] <= temperatures[i]:
                    counter += 1
                    #print(counter)                        
                else:
                    break 
            if (counter+i) < (len(temperatures)): #debug
                output.append(counter)                
            else:
                output.append(0)
            
            i+= 1
        
        output.append(0)
        return output
        """
"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
   Hide Hint #1  
If the temperature is say, 70 today, then in the future a warmer temperature must be either 71, 72, 73, ..., 99, or 100. We could remember when all of them occur next.
"""