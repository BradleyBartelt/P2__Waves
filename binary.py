
class Binaryclass:

    def __init__(self, input):
        if input < 2 or input > 50:
            raise ValueError("Series must be between 2 and 100")

        self.input = input
        self.binary_num = []
        self.conversion()
        self.total = ""


    def conversion(self):
        value = self.input

        while value >= 1:
            remainder = value%2
            value = value / 2
            value = value - 0.1
            value = round(value)
            self.binary_num.insert(0,remainder)

        for i in self.binary_num():
            self.total = self.total + str(i)


    """Getters with decorator to allow . notation access"""
    @property
    def series(self):
        return self.input

    @property
    def list(self):
        return self.binary_num

    @property
    def totally(self):
        return self.total


# Tester Code
if __name__ == "__main__":

    n = 10
    '''Constructor of Class object'''
    binaryclass = Binaryclass(n)

    '''Using getters to obtain data from object'''
    print(f"Fibonacci number for {n} = {binaryclass.series}")
    print(f"Fibonacci series for {n} = {binaryclass.list}")
    print(binaryclass.totally)

    '''Using method to get data from object
    for i in range(n):
        print(f"Fibonacci sequence {i + 1} = {binaryclass.get_sequence(i)}")
    '''