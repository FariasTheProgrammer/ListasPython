a = 80000
b = 200000
x = 0

while a <= b:
    a = a + a * 0.03  
    b = b + b * 0.015  
    x = x + 1  

print(x)
