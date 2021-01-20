# 0 ~ 1 float: radix sort encoder / decoder
# Type 0.1 0.01 0.001 allowed

def countingSort(arr, exp1):
    n = len(arr)
    output = [0]*(n)
    count = [0]*(10)

    for i in range(0, n):
        index = (arr[i]/exp1)
        count[int(index%10)] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    i = n-1
    while i>=0:
        index = arr[i] / exp1
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index%10)] -= 1
        i -= 1
    i = 0
    for i in range(0, n):
        arr[i] = output[i]


# Method to do Radix Sort
def radixSort(arr):
    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *= 10

# Driver code
# arr = [110, 454, 751, 903, 8302, 234, 2543, 660]

arr = [0.001, 0.0001, 0.1]
enc_arr = []
dec_arr = []

for i in arr:
    number_dec = str(i - int(i))[2:]
    # print(number_dec)
    enc = int(i * ((10 ** len(number_dec)) ** 2))
    # print(enc)
    enc_arr.append(enc)

radixSort(enc_arr)

for i in range(len(enc_arr)):
    print(enc_arr[i])

for i in enc_arr:
    dec = (i * 1 / (i ** 2))
    dec_arr.append(dec)

for i in range(len(dec_arr)):
    print(dec_arr[i])
