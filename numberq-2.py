"""# convert temperature celsius to fahrenheit
c=int(input("Enter temperature in celsius"))
f=(c*(9/5))+32
print("The converted value is ",f," fahrenheit")"""


#Fibonnaci series
n = int(input("Enter a number: "))
a, b = 0, 1

print("Fibonacci Series:")
for _ in range(n):
    print(a)
    a, b = b, a + b
