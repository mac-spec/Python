# convert temperature celsius to fahrenheit
c=int(input("Enter temperature in celsius"))
f=(c*(9/5))+32
print("The converted value is ",f," fahrenheit")


#Fibonnaci series
n = int(input("Enter a number: "))
a, b = 0, 1

print("Fibonacci Series:")
for _ in range(n):
    print(a)
    a, b = b, a + b


#Armstrong number
a=int(input())
b=a
s=0
while b > 0:
    d=b%10
    c=d ** 3
    s=s+c
    b//=10
if s==a:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")

#armstrong number for a particular interval
e = int(input())
upper_limit = int(input()) 

for a in range(e, upper_limit + 1):
    order = len(str(a))
    s = 0
    b = a
    while b > 0:
        digit = b % 10 
        s += digit ** order
        b //= 10
    
   
    if s == a:
        print(a)
