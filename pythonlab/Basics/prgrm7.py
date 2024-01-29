#string operations:

inputStr = input("Enter name: ")
print("Character Count: ",len(inputStr))
print("Word Count: ",len(inputStr.split()))
print(inputStr," in uppercase: ",inputStr.upper())
print(inputStr," in lowercase: ",inputStr.lower())
print("E in ",inputStr," is (1/-1): ",inputStr.find("E"))

tempStr = "Hello World"
print("Temp String: ",tempStr)
print("String slicing with two params: ",tempStr[0:len(tempStr)])
print("string slicing with three params: ",tempStr[0:len(tempStr):2])

li = ["1","2"]
print("String join: ",tempStr.join(li))