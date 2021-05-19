
class Conversionclass:

    def __init__(self, input, select):

        self._input = input
        self.converted_num = []
        self.select = select
        self.conversion()


    def conversion(self):
        value = self._input

        if self.select == "Binary":
            while value >= 1:
                remainder = value%2
                value = value / 2
                value = value - 0.1
                value = round(value)
                self.converted_num.insert(0,remainder)
        else:
            if value <= 9:
                self.converted_num.insert(0,value)
            else:
                while value >= 1:
                    remainder = value%16
                    value = value // 16
                    if remainder == 10:
                        remainder = "A"
                    if remainder == 11:
                        remainder = "B"
                    if remainder == 12:
                        remainder = "C"
                    if remainder == 13:
                        remainder = "D"
                    if remainder == 14:
                        remainder = "E"
                    if remainder == 15:
                        remainder = "F"
                    self.converted_num.insert(0,remainder)




    """Getters with decorator to allow . notation access"""
    @property
    def input(self):
        return self._input

    @property
    def list(self):
        return self.converted_num


