print("**Assignment 2**")

## Finding Greatest Number between three using condition (IF/ELSE)

a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
c = int(input("Enter c number: "))
if a>b and a>c:
    print("the largest number is ",a)
elif b>a and b>c:
    print("the largest number is ",b)
else :
    print("the largest number is ",c)