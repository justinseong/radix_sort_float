def lcm(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    for x in range(num2, num1*num2+1, num2):
        if x % num1 == 0:
            return x

print(lcm(6,8))

# Least Common Denominator