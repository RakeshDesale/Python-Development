// Program to check whether the given number is even or odd
//Input Format
//number n
//Constraints
//n value must be >=0
//Output Format
//even or odd invalid
//Sample Input 0
//12
//Sample Output 0
//even
//Sample Input 1
//13
//Sample Output 1
//odd


//Program:
  
  n=int(input())
  print("invalid" if n<0 else("even" if n%2==0 else "odd"))
