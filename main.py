import json
import math

jsonFile = '{"delay":500,"layers": [{"name":"N1", "ue":8, "ueAlias":"UE8","attenuation":20,"x":4, "y":0}, {"name":"P1", "ue":8, "ueAlias":"UE8", "attenuation":19.0, "x":0, "y":3}]}'
data = json.loads(jsonFile)


def ParseJSON(data):
    delay = data["delay"]

    layer_N = data["layers"][0]

    name_N = layer_N["name"]
    ue_N = layer_N["ue"]
    #temp = ''
    #for i in layer_N["ueAlias"]:
    #    if i.isdigit():
    #        temp += i
    #ueAlias_N = int(temp)
    ueAlias_N = layer_N["ueAlias"]
    attenuation_N = float(layer_N["attenuation"])
    x_N = int(layer_N["x"])
    y_N = int(layer_N["y"])

    layer_P = data["layers"][1]

    name_P = layer_P["name"]
    ue_P = layer_P["ue"]
    #temp = ''
    #for i in layer_P["ueAlias"]:
    #    if i.isdigit():
    #        temp += i
    #ueAlias_P = int(temp)
    ueAlias_P = layer_P["ueAlias"]
    attenuation_P = float(layer_P["attenuation"])
    x_P = int(layer_P["x"])
    y_P = int(layer_P["y"])

    array_N = [name_N, x_N, y_N]
    array_P = [name_P, x_P, y_P]

    #print(array_N)
    #print(array_P)

    return delay, array_N, array_P


def SwitchPosition(array):
    
    temp = ''
    for i in str(array[0]):
        if i.isdigit():
            temp += i
    layer = int(temp)
    column = array[1]
    row = array[2]

    match layer:
        case 1:
            SW_10x_index = 101
        case 2:
            SW_10x_index = 102
        case 3:
            SW_10x_index = 103
        case 4:
            SW_10x_index = 104
        case 5:
            SW_10x_index = 105
        case 6:
            SW_10x_index = 106
        case 7:
            SW_10x_index = 107
        case 8:
            SW_10x_index = 108

    SW_10x_pos = (column - 1) % 4
    match row:
        case 1:
            SW_10x_pos += 4
        case 2:
            SW_10x_pos += 8
        case 3:
            SW_10x_pos += 12

    SW_20x_index = (column-1) % 4 + row * 4 + 200
    SW_20x_pos = (column-1) // 4 + 1

    return SW_10x_index, SW_10x_pos, SW_20x_index, SW_20x_pos


def SwPosToPXI(SwitchPosition):
    SW_10x_index = SwitchPosition[0] 
    SW_10x_pos = SwitchPosition[1]
    SW_20x_index = SwitchPosition[2]
    SW_20x_pos = SwitchPosition[3]

    PXI_slot_1 = bin(SW_10x_pos - 1)[-4:]

    return PXI_slot_1


def ToBinary(number):
    bin_arr = []
    bin_num = str(bin(number).replace("0b", ""))

    for i in bin_num:
        bin_arr.append(int(i))

    return bin_arr


def Main(number):
    print(SwitchPosition(ParseJSON(data)[1]))
    return number

Main(0)
