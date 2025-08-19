num1=float(input("enter the first number"))
num2=float(input("enter the second number"))
operation=(input("enter your preferred operation"))
if operation=="+":
    output=num1+num2
    print("the output is:", output)
elif operation=="-":
    output=num1-num2
    print("the output is:", output)
elif operation=="*":
    output=num1*num2
    print("the output is:", output)
elif operation=="//":
    output=num1//num2
    print("the output is:", output)
elif operation=="**":
    output=num1**num2
    print("the output is:", output)
elif operation=="%":
    output=num1%num2
    print("the output is:", output)
else:
    print("invalid operation")