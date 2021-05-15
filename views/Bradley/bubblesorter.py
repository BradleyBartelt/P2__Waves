
class Listerclass:

    def __init__(self, input):
        self.final = []
        self.numberlist = []
        self._input = input
        self.conversion()


    def conversion(self):
        numberlist = self._input
        if len(numberlist) > 0:
            for i in range(len(numberlist)):
                numberlist[i] = int(numberlist[i])

        a = 0
        b = 1
        x = 1
        good = 0
        listlength = len(numberlist)
        goodlength = listlength - 1
        while x == 1:
            if numberlist[a] > numberlist[b]:
                addition = numberlist[a]
                del numberlist[a]
                numberlist.insert(b,addition)
                good = 0
            else:
                good = good + 1
            a = a + 1
            b = b + 1
            if b == listlength:
                a = 0
                b = 1
            if good == goodlength:
                x = 0
                self.final = numberlist


    @property
    def input(self):
        return self._input

    @property
    def list(self):
        return self.final







