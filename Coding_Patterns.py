# Q1 Input: ‘N’ = 3

Output: 
* * *
* * *
* * *

Solution 1:-
for i in range(n):
    print('* ' * n)

Solution 2:-
for i in range(n):
    for j in range(n):
        print('*' , end = ' ')
    print()


__________________________________________________
#Q2 Input:  ‘N’ = 3

Output: 
* 
* *
* * *

Solution 1:
  nn = 3
for i in range(nn+1):
    print('* ' * i)
  
Solution 2:
for i in range(n):
    for j in range(i+1):
        print('*', end = ' ')
    print()
___________________________________________________
#Q3 Input: ‘N’ = 3

Output: 
1
1 2 
1 2 3

    for i in range(n):
        for j in range(i + 1):
            print(j+1, end = ' ')
        print()
_________________________________________________
#Q4.Input: ‘N’ = 3

Output: 
1
2 2 
3 3 3

    for i in range(n):
        for j in range(i+1):
            print(i+1, end = ' ')
        print()

_______________________________________________
#Q5.Input: ‘N’ = 3

Output: 
* * *
* *
*

  
Solution 1:
    for i in range(n,-1,-1):
        for j in range(i):
            print('*' , end = ' ')
        print()

Solution 2:
for i in range(n-1,-1,-1):
    print('* ' * i)
_____________________________________________
#Q6 Input: ‘N’ = 3

Output: 

1 2 3
1 2
1

    for i in range(n,-1,-1):
       for j in range(i):
          print(j+1, end=' ')
       print()

______________________________________________
#q7 
  *  
 *** 
*****

    for i in range(n):
        print(' ' * (n - i -1) + '*' * (2 * i + 1))

________________________________________________
#Q8
*****
 ***
  *
    for i in range(n-1, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    pass

__________________________________________
#Q9 
  *
 ***
*****
*****
 ***
  *

    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    for i in range(n - 1, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

__________________________________________________
#Q10
*
**
***
**
*

    for i in range(n):
        print('*' * i)
    for i in range(n , -1, -1):
        print('*' * i)
______________________________________________
#Q11
1
0 1
1 0 1

    for i in range (n):
        for j in range(i + 1):
            print((i + j + 1) % 2 , end =' ')
        print()

_______________________________________
#Q12
1
2 3
4 5 6
    cn = 1
    for i in range(n):
       for j in range(i+1):
          print(cn, end = ' ')
          cn += 1
       print()
____________________________________________
#Q13
A
A B
A B C

    for i in range(n):
        for j in range(i + 1):
           print(chr(65 + j), end = ' ')
        print()
____________________________________________
#q14
1       1 
1 2    2 1 
1 2 3 3 2 1 

n = 3  # Number of rows
for i in range(1, n + 1):
    # Print increasing numbers
    for j in range(1, i + 1):
        print(j, end=" ")
    
    # Print spaces in the middle
    for j in range(2 * (n - i) - 1):
        print(" ", end=" ")
    
    # Print decreasing numbers
    for j in range(i, 0, -1):
        print(j, end=" ")
    
    print()

__________________________________________
#q15
A 
B B 
C C C 
D D D D
for i in range(n):
   for j in range(i + 1):
         print(chr(65 + i), end = ' ')
   print()

____________________________________
#q16
    A
  A B A
A B C B A
n = 3
for i in range(n):
     print(' ' * (n - i - 1), end = '')
     for j in range(i + 1):
         print(chr(65 + j), end = ' ')
     for j in range(i - 1, -1, -1):
         print(chr(65 + j), end = ' ')
     print()
_______________________________________
#Q17
E 
D E 
C D E 
B C D E 
A B C D E 

for i in range(n):
    start_char = chr((65 + (n-1)) - i)
    for j in range(i+1):
        row = chr(ord(start_char) + j)
        print(' '.join(row), end = ' ')
    print()

_____________________________________________
#Q18
C
C B 
C B A
for i in range(n):
    # Loop to print each character in the row
    for j in range(i + 1):
        print(chr(65 + (n-1) - j), end=" ")  # 67 is the ASCII value of 'C'
    print()  




