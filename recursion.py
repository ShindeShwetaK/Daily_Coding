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
  
------------------------------
def reverse_array(arr, l=0, r=None):
    if r is None:
        r = len(arr) - 1
    
    if l >= r:
        return arr  # Base case: when left index meets or crosses right index
    
    arr[l], arr[r] = arr[r], arr[l]  # Swap elements
    
    return reverse_array(arr, l + 1, r - 1)  # Recursive call

# Example usage:
arr = [1, 2, 3, 4, 5]
print(reverse_array(arr))  # Output: [5, 4, 3, 2, 1]

-------------------------------
class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr):
        #  code here
        len_arr = (len(arr))+1
        output = [0] * len_arr
        
        for i in arr:
            output[i] += 1
            
        return output[1:]
arr = [1, 1, 2, 2, 3, 4]
[2, 2, 1, 1, 0, 0] Count the occurances of number in the array
________________________________________
