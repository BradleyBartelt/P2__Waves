# binary_string = "1010"
#
# decimal_representation = int(binary_string, 2)
# hexadecimal_string = hex(decimal_representation)
#
# print(hexadecimal_string)

def convert(binary_string):
    decimal_representation = int(binary_string, 2)
    hexadecimal_string = hex(decimal_representation)
    return hexadecimal_string

if __name__=="__main__":

    binary_string = "0001101011000101"
    convert(binary_string)

    print(convert(binary_string))