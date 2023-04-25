# IPP
Program do zarządzania pomiarami OTA


## Function ParseJSON

**The function reads individual data from the given json file and returns the values necessary for the further operation of the program**

### Arguments:
- data - the function takes as an argument a JSON file containing information about the parameters of the measurements performed

### Return:
- delay - value of measurement time performed with a specific set of parameters
- array_N - array of measurement parameters for negative polarity (name of the layer, x cords, y cords)
- array_P - array of measurement parameters for positive polarity (name of the layer, x cords, y cords)


## Function SwitchPosition

**The function translates input parameters to the position of binary switches located in the hardware**

### Arguments:
- array - array of one set measurements parameters (for positive and negative polarity, you must use it twice)

### Return
- SW_10x_index - 1 of 4 switches that transfers data to the hardware
- SW_10x_pos - as above
- SW_20x_index - as above
- SW_20x_pos - as above

## Function SwPosToPXI

**The function translates switch positions into PXI values that are passed directly to the LabVIEV measurement management software**

### Arguments: 
- SwitchPosition - array of position of 4 switches from previous function

### Return:
- [x] PXI_slot_1 - 1 of 3 PXI slots
- [ ]PXI_slot_2 - as above
- [ ]PXI_slot_3 - as above
