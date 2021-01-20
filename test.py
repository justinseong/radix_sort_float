# 0 ~ 1 float: radix sort encoder / decoder

number = 0.001

number_dec = str(number-int(number))[2:]
print(number_dec)

enc = int(number * ((10**len(number_dec))**2))
print(enc) # Encode

dec = (enc * 1/(enc**2))
print(dec) # Decode