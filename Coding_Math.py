N= 8987
Find the count of the numbers

len(str(N))

Solution2:
count = 0
for i in str(N):
  count += 1
print(count)

Solution2:
count = 0
while n>0:
    n //= 10
    count += 1
print(count)
_______________________________
#Q Find the number of digits of ‘n’ that evenly divide ‘n’.
Note:
A digit evenly divides ‘n’ if it leaves no remainder when dividing ‘n’.
Example:
Input: ‘n’ = 336
Output: 3
Explanation:
336 is divisible by both ‘3’ and ‘6’. 

temp = n
count = 0
while temp > 0:
  digit = temp % 10
  if digit != 0 and n % digit == 0:
    count += 1
  temp //= 10
  return(count)
__________________________________
#Q7 Reverse the give number
#https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            is_negative = True
            x*=-1
        digit = 0
        while x>0:
            digit = (digit*10) + (x % 10)
            x //= 10

        if digit >2  ** 31 - 1:
            return 0
        
        if is_negative:
            return -digit
        else:
            return digit
____________________________________________
# Is Palindrom
class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        if x<0:
            return False

        digit = 0
        while x>0:
            digit = (digit * 10) + ( x % 10)
            x //= 10

        if original == digit:
            return True
        else:
            return False

  _____________________________________________
Find the GCD of 12 and 18:

Divisors of 12: {1, 2, 3, 4, 6, 12}
Divisors of 18: {1, 2, 3, 6, 9, 18}
Common divisors: {1, 2, 3, 6}
Greatest Common Divisor: 6
18 ÷ 12 = 1 remainder 6  
12 ÷ 6 = 2 remainder 0  
GCD = 6  

Find the LCM of 12 and 18:

Multiples of 12: {12, 24, 36, 48, ...}
Multiples of 18: {18, 36, 54, ...}
Common multiples: {36, 72, ...}
Smallest Common Multiple: 36
For 12 and 18:
6 = GCD
LCM(12,18)=  12×18 / 6
= 216 / 6 =36

class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        # code here
        result = []
        gcd = 1
        lcm = 1
        
        og_a = a
        og_b = b
        
        while b:
            a, b = b , a % b
        gcd = a
        
        lcm = (og_a * og_b) // gcd
        
        return [lcm, gcd]
_____________________________________________
#Amstrong number
        len_n = len(str(n))
        og_n = n
        sum = 0

        while n:
            sum += (n % 10) ** len_n
            n //= 10

        return sum == og_n

________________________________________
#Prime Number Yes or No
n = 5
if n <= 1:
    print("NO")
if n == 2:
    print('YES')

for i in range(2,n):
    if n % i == 0:
        print("NO")
    
print('YES')
_______________________________
#Sum of divisers
def sum_of_divisors(n):
    # First loop to calculate sum of divisors for each number from 1 to n
    divisor_sums = []
    for i in range(1, n + 1):
        divisor_sum = 0
        for j in range(1, i + 1):
            if i % j == 0:  # Check if j is a divisor of i
                divisor_sum += j
        divisor_sums.append(divisor_sum)
    
    # Second loop to sum all the divisor sums
    total = 0
    for sum_value in divisor_sums:
        total += sum_value

    return total

# Example usage
n = 4
print(sum_of_divisors(n))  # Output: 15
