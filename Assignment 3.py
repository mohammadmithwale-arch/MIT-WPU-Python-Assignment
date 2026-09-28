a = int(input("enter the first side:"))
b = int(input("enter the second side:"))
c = int(input("enter the third side:"))
def right_triangle(a,b,c):
    if a>b and a>c:
        return b*b + c*c == a*a
    elif b>a and b>c:
        return b * b == c * c + a * a
    else :
        return c * c == a * a + b * b

if right_triangle(a,b,c):
    print("TRIANGLE IS A RIGHT TRIANGLE")
else:
    print("TRIANGLE IS NOT A RIGHT TRIANGLE")
