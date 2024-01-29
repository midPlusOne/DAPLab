# import keyword
# #=====================================================================
# print("========== PYTHON IDENTIFIER ==========")
# a=10
# print("\ta is an identifier")
# #=====================================================================
# print("\n========== PYTHON VARIABLES ==========")
# name="Anirudha B G Somayaji"
# booleanValue=True
# fltNum=10.2
# print("\tVariables are: ",name,booleanValue,fltNum)
# #=====================================================================
# print("\n========== PYTHON KEYWORDS ==========")
# print("\tThe python keywords are: \n",keyword.kwlist)
# #=====================================================================
# print("\n========== PYTHON EXPRESSIONS ==========")
# print("\t==== Constant Expression ====")
# x=15+14.3
# print("\tx = 15 + 14.3 = ",x)
# print("\t==== Arithmetic expression ====")
# num1=10
# num2=20
# add=num1+num2
# sub=num1-num2
# mul=num1*num2
# div=num1/num2
# print("\tadd = num1 + num2 = ",add)
# print("\tsub = num1 - num2 = ",sub)
# print("\tmul = num1 * num2 = ",mul)
# print("\tdiv = num1 / num2 = ",div)
# print("\t==== Integral Expression ====")
# num3=10.2
# res=num1+int(num3)
# print("\tres = num1 + int(num3) = ",res)
# print("\t==== Floating Expression ====")
# print("\tdiv = num1 / num2 = ",div)
# print("\t==== Relational Expression ====")
# print("\t(num1 > num2) <= (num2 > num1) = ",(num1 > num2) <= (num2 > num1))
# print("\t==== Logical Expression ====")
# num4=num1 == num2
# num5=num1 > num2
# res1=num4 and num5
# res2= num4 or num5
# res3=not num4
# print("\tres1 = num4 and num5 = ",res1)
# print("\tres2 = num4 or num5 = ",res2)
# print("\tres3 = not num5 = ",res3)
# #=====================================================================
# print("\n========== PYTHON OPERATORS ==========")
# print("\t==== Arithmetic Operators ====")
# print("\tadd = num1 + num2 = ",add)
# print("\tsub = num1 - num2 = ",sub)
# print("\tmul = num1 * num2 = ",mul)
# print("\tdiv = num1 / num2 = ",div)
# print("\tflrdiv = num1 // num2 = ",num1//num2)
# print("\tremainder = num1 % num2 = ",num1 % num2)
# print("\tpower = num1 ** 2 = ",num1 ** 2)
# print("\t==== Assignment Operator ====")
# num1=10
# print("\tnum1 = ",num1)
# num1+=10
# print("\tnum1 += 10 = ",num1)
# num1-=10
# print("\tnum1 -= 10 = ",num1)
# num1*=10
# print("\tnum1 *= 10 = ",num1)
# num1/=10
# print("\tnum1 /= 10 = ",num1)
# num1%=10
# print("\tnum1 %= 10 = ",num1)
# print("\t==== Comparision Operator ====")
# print("\tnum1 > num2 = ",num1 > num2)
# print("\tnum1 >= num2 = ",num1 >= num2)
# print("\tnum1 < num2 = ",num1 < num2)
# print("\tnum1 <= num2 = ",num1 <= num2)
# print("\tnum1 == num2 = ",num1 == num2)
# print("\tnum1 != num2 = ",num1 != num2)
# print("\t==== Logical Operator ====")
# print("\tres1 = num4 and num5 = ",res1)
# print("\tres2 = num4 or num5 = ",res2)
# print("\tres3 = not num5 = ",res3)
# print("\t==== Identity Operator ====")
# print("\tres1 is num1 = ",res1 is num1)
# print("\tres1 is not num1 = ",res1 is not num1)
# print("\t==== Membership Operator ====")
# X=1
# List=[1,2,3,4,5,6]
# print("\tX in List = ",X in List)
# print("\tX not in List = ", X not in List)

# string2 = '''
# Hello my name is anirudha
# i am noob
# '''

# print(string2)


# print([0] * 4)

t = 0
c = 0
while True:
    num = input('Enter value: ')
    if num == 'done': break
    val = float(num)
    t += val
    c += 1

avg = t / c
print(avg)
