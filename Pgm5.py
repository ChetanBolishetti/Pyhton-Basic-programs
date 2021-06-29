
try:
    a = int(input("Enter number one "))
    b = int(input("Enter number two "))
    c=a/b
    print("Answer = ",c)
except ZeroDivisionError as e:
    print("Cannot divide by zero",e)
except Exception as e:
    print(e)