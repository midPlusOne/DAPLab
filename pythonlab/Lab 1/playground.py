#Write a python program for linear search

def searchIt(li,k):
    for i in range(len(li)):
        if li[i] == k:
            return i
    return -1

li = []
size = int(input("Enter size: "))

for i in range(0,size):
    val = int(input(f"Enter value at {i}: "))
    li.append(val)

print("Given List is: ",li)
k = int(input("Enter Key: "))

found = searchIt(li,k)

if found == -1:
    print("Key not found")
else:
    print("Key found at: ",found)