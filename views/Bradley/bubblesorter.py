class Listerclass:

    def __init__(self, input):

        self._input = input
        self.conversion()
        self.numberlist = []
        self.numberlist.insert(0,self._input)

    def conversion(self):
        a = 0
        b = 1
        x = 1
        good = 0
        listlength = len(self.numberlist)
        goodlength = listlength - 1
        while x == 1:
            if self.numberlist[a] > self.numberlist[b]:
                addition = self.numberlist[a]
                del self.numberlist[a]
                self.numberlist.insert(b,addition)
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


    @property
    def input(self):
        return self._input

    @property
    def list(self):
        return self.numberlist







