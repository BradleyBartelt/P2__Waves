# Python3 program to convert
# Hexadecimal number to Binary

# Function to convert
# Hexadecimal to Binary Number

#  create the contructor
class Conversion:
    def __init__(self, user_input, hex_input):
        '''intial, increment, increment lneght'''
        '''validator'''
        '''delcaring valirables'''

        '''input'''
        self._input = user_input
        self._hex_input = str(hex_input)

        '''output'''
        self._list = []
        self._binary = ''
        '''dictonary maybes, input number, hex, binary'''

        self.HexToBin()

    '''helper funcitons (middle man, logic here)'''
    def HexToBin(self):
        hexdec = self._hex_input
        #print("in the helper func:" +str(hexdec))
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
        self._binary = self._binary + a

    '''getter (passing values to display, no logic here)'''
    @property
    def OneToOne(self):
        return self._input

    @property
    def BinFromHex(self):
        return self._binary

def convert(binary_string):
    decimal_representation = int(binary_string, 2)
    hexadecimal_string = hex(decimal_representation)
    return hexadecimal_string

# Driver code
if __name__=="__main__":
    input = 1
    hex_string = "1AC5"
    conversion = Conversion(input, hex_string)
    print("you inputed: " +str(conversion.OneToOne))
    print("print the binary from the hex: " +str(conversion.BinFromHex))
