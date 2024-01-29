a=10
b=20
c=23
d=14
res=a*b-(b//d)*c-(d+a)
print("res = a * b - (b // d) * c - (d + a)")
print("step1: a * b = 10 * 20 = 200")
print("step2: b // d = 20 // 14 = 1")
print("step3: (b // d) * c = 1 * 23 = 23")
print("step4: d + a = 14 + 10 = 24")
print("step5: - (b // d) * c - (d + a) = -23 -24 = 47")
print("step6: a * b - (b // d) * c - (d + a) = 200 - 47 = ",res)
