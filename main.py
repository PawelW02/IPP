import json

jsonFile = '{"delay":500,"layers": [{"name":"N1", "ue":8, "ueAlias":"UE8","attenuation":20,"x":0, "y":3}, {"name":"P1", "ue":8, "ueAlias":"UE8", "attenuation":19.0, "x":0, "y":3}]}'
data = json.loads(jsonFile)
delay = data["delay"]

layer_N = data["layers"][0]

name_N = layer_N["name"]
ue_N = layer_N["ue"]
temp = ''
for i in layer_N["ueAlias"]:
    if i.isdigit():
        temp += i
ueAlias_N = int(temp)
attenuation_N = float(layer_N["attenuation"])
x_N = int(layer_N["x"])
y_N = int(layer_N["y"])

layer_P = data["layers"][1]

name_P = layer_P["name"]
ue_P = layer_P["ue"]
temp = ''
for i in layer_P["ueAlias"]:
    if i.isdigit():
        temp += i
ueAlias_P = int(temp)
attenuation_P = float(layer_P["attenuation"])
x_P = int(layer_P["x"])
y_P = int(layer_P["y"])

array_N = [name_N, ue_N, ueAlias_N, attenuation_N, x_N, y_N]
array_P = [name_P, ue_P, ueAlias_P, attenuation_P, x_P, y_P]

print(array_N)
print(array_P)

def Main(number):
    return number

def ToBinary(number):
    bin_arr = []
    bin_num = str(bin(number).replace("0b", ""))

    for i in bin_num:
        bin_arr.append(int(i))

    return bin_arr

#print(ToBinary(987654321))