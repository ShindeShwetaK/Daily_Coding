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
#Q6 





