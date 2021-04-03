# Python3 program to convert
# Hexadecimal number to Binary

# Function to convert
# Hexadecimal to Binary Number

#  create the contructor
class Conversion:
    def __init__(self, user_input, user_list):
        '''intial, increment, increment lneght'''
        '''validator'''
        '''delcaring valirables'''

        '''input'''
        self._input = user_input
        self._input_list = user_list
        #self._hex_input = str(hex_input)

        '''output'''
        self._list = []
        self._binary = ''
        self._hex = 0
        '''dictonary maybes, input number, hex, binary'''

        # attempted here to do a nested helper function
        b = ''
        self.DecToHex()

        self.HexToBin(b)
        self.AppendDict()


    '''helper funcitons (middle man, logic here)'''
    def DecToHex(self):
        input = self._input
        self._hex = hex(input)

    def HexToBin(self, b):
        #hexdec = self._hex_input
        #hexdec = str(self._hex)
        #print("in the helper func:" +str(hexdec))

        # if b does have a values
        if b != '':
            hexdec = str(hex(b))
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
        else:
            hexdec = str(self._hex)
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

    def AppendDict(self):
        used_list = self._input_list
        # for the numbers in the input list

        # ensuring that the increment is base zeto
        a = 0
        for i in self._input_list:
            # creating a dicto
            current_values = used_list[a]
            number = {
                "input": str(current_values),
                "hex": str(hex(current_values)),
                "binary": str(bin(current_values))

            }
            self._list.append(number)
            a = a + 1

    '''getter (passing values to display, no logic here)'''
    @property
    def OneToOne(self):
        return self._input

    @property
    def BinFromHex(self):
        return self._binary

    @property
    def HexOut(self):
        return self._hex

    @property
    def ReturnList(self):
        return self._list

def convert(binary_string):
    decimal_representation = int(binary_string, 2)
    hexadecimal_string = hex(decimal_representation)
    return hexadecimal_string

# Driver code
if __name__=="__main__":
    input = 100
    hex_string = "1AC5"
    input_list = [1,2,3,4,5,6,7,8]
    conversion = Conversion(input, input_list)
    print("you inputed: " +str(conversion.OneToOne))
    print("your input is equivalent to hex: " +str(conversion.HexOut))
    print("print the binary from the hex: " +str(conversion.BinFromHex))

    print('-----------------')
    print('the vlaues within the conversions of the list: ' +str(conversion._list))
