1 2 3 4 5 6 7....
class Solution:    
    #Complete this function
    def printNos(self,n):
        #Your code here
        if n<=0:
            return
        
        self.printNos(n - 1)
        print(n, end = ' ')

  ---------------------------------------
GFG GFG GFG GFG GFG...
class Solution:
    def printGfg(self, n):
        # Code here
        if n<=0:
            return
        
        self.printGfg(n-1)
        print('GFG', end =' ')

----------------------------------------
10 9 8 7 6 5.....
class Solution:
    def printNos(self, n):
        # Code here
        if n <= 0:
            return
        
        print(n, end = " ")
        self.printNos(n-1)
  -------------------------------------
n =5
Input: n = 5
Output: 225
Explanation: 13 + 23 + 33 + 43 + 53 = 225
class Solution:
    def sumOfSeries(self,n):
        #code here
        if n == 0:
            return 0
        
        return n ** 3 + self.sumOfSeries(n - 1)
  
