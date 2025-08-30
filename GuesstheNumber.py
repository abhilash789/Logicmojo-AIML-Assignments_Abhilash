import random

print("Guess the Number Between 1- 100 in 10 attempts")

num =random.randint(1,100)
print(num)
i=1
while(i<=10):
    
    g_num = int(input("Guess the Number : "))
    if g_num ==  num:
        print("Congratulations Your Guess Correct")
        break
    elif g_num > num:
        print("Actual Number is less than the current Number , Try again...")
        i+=1
    else:
       print("Actual Number is greater than the current Number, Try again...")
       i+=1
    attempts=11-i
    print("attempts remaining :" + str(attempts))   


if i==11:
    print("Game Over")


