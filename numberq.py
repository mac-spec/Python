#To find the largest among 3 numbers
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if a>b and a>c:
   print(a," is the greatest number")
elif b>c:
   print(b," is the greatest number")
else:
   print(c," is the greatest number")

#check prime number
n=int(input("Enter a number to check if it is prime "))
c=0
for i in range (1,n+1):
   if(n%i==0):
    c+=1
if(c==2):
        print("Yes!! The number is prime")
else:
                print("NO!! The number is not prime")


#Generate random int
import random
a=random.randint(-100,-1)
print(a)



#Prime numbers in an interval
n=int(input("Enter starting interval to print the prime numbers "))
m=int(input("Enter ending interval to print the prime numbers  "))
for i in range (n,m+1):
   c=0
   for j in range (1,i+1):
     if i%j==0:
      c+=1
   if(c==2):
    print(i)


