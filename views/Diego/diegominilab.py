class Pi:
    """Initializer of class takes series parameter and returns Class Objectg"""
    def __init__(self, number):
        """Built in validation and exception"""
        if number < 2 or number > 100:
            raise ValueError("Decimal place must be between 2 and 100")
        self._number = number
        self._list = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.calcPi()
        self._lastNumber
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

    """Algorithm for building Fibonacci sequence, this id called from __init__"""
    def calcPi(self):  # Generator function


        q, r, t, k, n, l = 1, 0, 1, 1, 3, 3

        decimal = self._number
        counter = 0
        number = ""
        while counter != decimal + 1:
            if 4 * q + r - t < n * t:
                # yield digit
                number = number + str(n)
                self.set_data(number)
                if counter == 0:
                    number = number + "."
                if decimal == counter:
                    self._lastNumber = n
                    break
                counter += 1
                nr = 9 * (r - n * t)
                n = ((5 * (3 * q + r)) // t) - 10 * n
                q *= 12
                r = nr
            else:
                nr = (4 * q + r) * l
                nn = (q * (3 * k) + 1 + (r * l)) // (t * l)
                q *= k
                t *= l
                l += 3
                k += 8
                n = nn
                r = nr



    """Method/Function to set Fibonacci data: list, dict, and dictID are instance variables of Class"""
    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1

    """Getters with decorator to allow . notation access"""
    @property
    def series(self):
        return self._number

    @property
    def list(self):
        return self._list

    @property
    def number(self):
        return self._list[self._dictID - 1]

    """Traditional Getter requires method access"""
    def get_sequence(self, nth):
        return self._dict[nth]

    @property
    def lastNumber(self):
        return self._lastNumber


if __name__ == "__main__":
    '''Value for testing'''
    n = 20
    '''Constructor of Class object'''

