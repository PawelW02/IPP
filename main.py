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

    return [delay, array_N, array_P]


def SwitchPosition(array):
    
    temp = ''
    for i in str(array[0]):
        if i.isdigit():
            temp += i
    layer = int(temp)
    column = array[1]
    row = array[2]

    if layer == 1:
        SW_10x_index = 101
    elif layer == 2:
        SW_10x_index = 102
    elif layer == 3:
        SW_10x_index = 103
    elif layer == 4:
        SW_10x_index = 101
    elif layer == 5:
        SW_10x_index = 105
    elif layer == 6:
        SW_10x_index = 106
    elif layer == 7:
        SW_10x_index = 107    
    elif layer == 8:
        SW_10x_index = 108

#    match layer:
#        case 1:
#            SW_10x_index = 101
#        case 2:
#            SW_10x_index = 102
#        case 3:
#            SW_10x_index = 103
#        case 4:
#            SW_10x_index = 104
#        case 5:
#            SW_10x_index = 105
#        case 6:
#            SW_10x_index = 106
#        case 7:
#            SW_10x_index = 107
#        case 8:
#            SW_10x_index = 108

    SW_10x_pos = (column - 1) % 4
    if row == 1:
        SW_10x_pos += 4
    elif row == 2:
        SW_10x_pos += 8
    elif row == 3:
        SW_10x_pos += 12
    #match row:
    #    case 1:
    #        SW_10x_pos += 4
    #    case 2:
    #        SW_10x_pos += 8
    #    case 3:
    #        SW_10x_pos += 12

    SW_20x_index = (column-1) % 4 + row * 4 + 200
    SW_20x_pos = (column-1) // 4 + 1

    return [SW_10x_index, SW_10x_pos, SW_20x_index, SW_20x_pos]


def SwPosToPXI(SwitchPosition):
    PXI_slot_1 = []
    PXI_slot_2 = [] 
    PXI_slot_3 = []
    for i in range(32):
        PXI_slot_1.append('0')
        PXI_slot_2.append('0')
        PXI_slot_3.append('0')
    SW_10x_index = SwitchPosition[0] 
    SW_10x_pos = SwitchPosition[1]
    SW_20x_index = SwitchPosition[2]
    SW_20x_pos = SwitchPosition[3]
    i1 = (SW_10x_index - 101) * 4
    i2 = (SW_20x_index - 201) * 4
    i3 = (SW_20x_index - 209) * 4

    if (SW_20x_index - 200) > 8:
        PXI_slot_3[i3:i3+4] = bin(SW_20x_pos - 1).replace("0b", "")[-4:]
    else:
        PXI_slot_2[i2:i2+4] = bin(SW_20x_pos - 1).replace("0b", "")[-4:]
    PXI_slot_1[i1:i1+4] = bin(SW_10x_pos - 1).replace("0b", "")[-4:]

    PXI_slot_1 = int("".join(PXI_slot_1),2)
    PXI_slot_2 = int("".join(PXI_slot_2),2)
    PXI_slot_3 = int("".join(PXI_slot_3),2)

    return [PXI_slot_1, PXI_slot_2, PXI_slot_3]


def ToBinary(number):
    bin_arr = []
    bin_num = str(bin(number).replace("0b", ""))

    for i in bin_num:
        bin_arr.append(int(i))

    return bin_arr


def Main():
    cords = ParseJSON(data)
    SWpos = SwitchPosition(cords[1])
    PXI_array = SwPosToPXI(SWpos)

    return PXI_array

def Slot_1():
    return Main()[0]
def Slot_2():
    return Main()[1]
def Slot_3():
    return Main()[2]


#print(Main())
#print(SwitchPosition(['N1', 3, 8]))
#print(SwPosToPXI([101, 14, 216, 14])[0])
print(Slot_1())
print(Slot_2())
print(Slot_3())