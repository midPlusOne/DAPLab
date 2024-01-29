print("Sum of 10 numbers using for loop and break")
sum1 = 0
for i in range(10):
    if(i == 5):
        print("Break: Used to break when i is equal to 5")
        break
    sum1 += i
print("sum is: ",sum1)
print("Sum of 10 numbers using while loop and continue")
sum2 = 0
i = 0
while i < 10:
    sum2 += i
    i += 1
    if(i == 5):
        print("Continue: used to skip the number 5 when i is equal to 5") 
        continue
print("sum  is: ",sum2)
print("if statements")

if sum1 == 10:
    if sum2 == 45:
        print("You are inside nested if")

if sum1 == 11:
    print("Hello")
elif sum1 == 10:
    print("You are inside elif")
else:
    print("Bye")

