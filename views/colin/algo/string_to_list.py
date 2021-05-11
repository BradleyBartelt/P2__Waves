def stringToList(string):
    output_list = string.split(",")
    return output_list

def stringTo3List(string):
    final_list = []
    output_list = string.split(",")
    #i = 0
    for i in range(0,len(output_list)):
        if i%2 != 0:
            print(output_list[i])
            pair_list.append(output_list[i])
            final_list.append(pair_list)
        else:
            # this is the part that will run first
            pair_list = []
            print(i)
            print(output_list[i])
            pair_list.append(output_list[i])

    return final_list

if __name__ == "__main__":

    # taking the input of the devices string and converting it into one large list
    input_string = "device1,164.00000095367432,108.10511779785156,device2,82.00000095367432,200.10511779785156,device3,247.00000095367432,197.10511779785156,device4,75.00000095367432,334.10511779785156,device5,290.0000009536743,327.10511779785156"
    print(stringToList(input_string))

    connection_string = "device1,device2,device2,device4,device1,device3,device3,device5"
    print(stringTo3List(connection_string))



