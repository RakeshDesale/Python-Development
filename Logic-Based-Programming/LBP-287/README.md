# Problem Statement:

Implement a program, it reads integers from the input device(until it gets -ve number) and put them into array. We define a hot number as any number whose last digit is 2, and cold number as any number that is less than 50. You have to modify the program such that<br>
if it is hot number replace by -1<br>
if it is cold number replace by -5<br>
if it is both hot and cold replace by -6<br>
else keep old number<br>

### Input Format

a sequence of int values

### Constraints

no

### Output Format

a sequence of int values

### Sample Input 0
```
92 61 13 42 -1
```
### Sample Output 0
```
-1 61 -5 -6
```
### Sample Input 1
```
11 12 85 96 82 -1
```
### Sample Output 1
```
-5 -6 85 96 -1
```
