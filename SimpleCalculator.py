Number1 = input("Enter the First Number : ")
Number2 = input("Enter the Second Number : ")

print("Operations that you can perform on these Number are : + , - , * , / ")

Operation= input("Enter the Operation to Perform from above : ")

answer=0
a=int(Number1)
b=int(Number2)

match Operation:
    case '+':
        answer = a+b
    case '-':
        answer =a-b
    case '*':
        answer =a*b
    case '/':
        answer= a/b 
    case _:
        input("invalid choice. Please enter the valid operator :")

print(answer)       