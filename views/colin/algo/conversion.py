# Python3 program to convert
# Hexadecimal number to Binary

# Function to convert
# Hexadecimal to Binary Number
"""def HexToBin(hexdec):

    for i in hexdec:
        if i == '0':
            print('0000', end = '')
        elif i == '1':
            print('0001', end = '')
        elif i == '2':
            print('0010', end = '')
        elif i == '3':
            print('0011', end = '')
        elif i == '4':
            print('0100', end = '')
        elif i == '5':
            print('0101', end = '')
        elif i == '6':
            print('0110', end = '')
        elif i == '7':
            print('0111', end = '')
        elif i == '8':
            print('1000', end = '')
        elif i == '9':
            print('1001', end = '')
        elif i == 'A' or i == 'a':
            print('1010', end = '')
        elif i == 'B' or i == 'b':
            print('1011', end = '')
        elif i == 'C' or i == 'c':
            print('1100', end = '')
        elif i == 'D' or i == 'd':
            print('1101', end = '')
        elif i == 'E' or i == 'e':
            print('1110', end = '')
        elif i == 'F' or i == 'f':
            print('1111', end = '')
        else:
            print("\nInvalid hexadecimal digit " +
                  str(hexdec[i]), end = '')
"""

def HexToBinValue(hexdec):
    a = ''
    for i in hexdec:
        if i == '0':
            a = a + '0000'
        elif i == '1':
            a = a + '0001'
        elif i == '2':
            a = a + '0010'
        elif i == '3':
            a = a + '0011'
        elif i == '4':
            a = a + '0100'
        elif i == '5':
            a = a + '0101'
        elif i == '6':
            a = a + '0110'
        elif i == '7':
            a = a + '0111'
        elif i == '8':
            a = a + '1000'
        elif i == '9':
            a = a + '1001'
        elif i == 'A' or i == 'a':
            a = a + '1010'
        elif i == 'B' or i == 'b':
            a = a + '1011'
        elif i == 'C' or i == 'c':
            a = a + '1100'
        elif i == 'D' or i == 'd':
            a = a + '1101'
        elif i == 'E' or i == 'e':
            a = a + '1110'
        elif i == 'F' or i == 'f':
            a = a + '0111'

    return a

def convert(binary_string):
    decimal_representation = int(binary_string, 2)
    hexadecimal_string = hex(decimal_representation)
    return hexadecimal_string

# Driver code
if __name__=="__main__":

    # Get the Hexadecimal number
    hexdec= "1AC5";

    print('input: '+str(hexdec))
    output = HexToBinValue(hexdec)
    # Convert HexaDecimal to Binary
    print("Equivalent Binary value is : " +str(output))


    print("")
    print("converting back ")
    #output = convert(str(HexToBin(hexdec)))
    output1 = convert(output)
    print(str(output1))

# This code is contributed by Rutvik_56