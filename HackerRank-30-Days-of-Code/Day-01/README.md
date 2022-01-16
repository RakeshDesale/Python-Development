# Day 1: Data Types

### Objective
Today, we're discussing data types. Check out the [Tutorial](https://www.hackerrank.com/challenges/30-data-types/tutorial) tab for learning materials and an instructional video!

### Task
Complete the code in the editor below. The variables ___i___, ___d___, and ___s___ are already declared and initialized for you. You must:

1. Declare __3__ variables: one of type int, one of type double, and one of type String.
2. Read __3__ lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your __3__ variables.
3. Use the __+__ operator to perform the following operations:
  <br>1. Print the sum of ___i___ plus your int variable on a new line.
  <br>2. Print the sum of ___d___ plus your double variable to a scale of one decimal place on a new line.
  <br>3. Concatenate ___s___ with the string you read as input and print the result on a new line.

__Note:__ If you are using a language that doesn't support using  for string concatenation (e.g.: C), you can just print one variable immediately following the other on the same line. The string provided in your editor must be printed first, immediately followed by the string you read as input.

### Input Format

The first line contains an integer that you must sum with ___i.___<br>
The second line contains a double that you must sum with ___d.___<br>
The third line contains a string that you must concatenate with ___s.___

### Output Format

Print the sum of both integers on the first line, the sum of both doubles (scaled to __1__ decimal place) on the second line, and then the two concatenated strings on the third line.

### Sample Input
```
12
4.0
is the best place to learn and practice coding!
```
### Sample Output
```
16
8.0
HackerRank is the best place to learn and practice coding!
```
### Explanation

When we sum the integers __4__ and __12__, we get the integer __16__.<br>
When we sum the floating-point numbers __4.0__ and __4.0__, we get __8.0__.<br>
When we concatenate `HackerRank` with `is the best place to learn and practice coding!`, we get `HackerRank is the best place to learn and practice coding!.`

__You will not pass this challenge if you attempt to assign the Sample Case values to your variables instead of following the instructions above and reading input from stdin.__
