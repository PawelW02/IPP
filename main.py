def Main(number):
    return number

def ToBinary(number):
    bin_arr = []
    bin_num = str(bin(number).replace("0b", ""))

    for i in bin_num:
        bin_arr.append(int(i))

    return bin_arr

print(ToBinary(987654321))