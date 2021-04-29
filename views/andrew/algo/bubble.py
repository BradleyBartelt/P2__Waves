class BubbleSort:
    def __init__(self, input_list,isString):

        # init/declare the variables
        self.input_list = input_list


        # init the outpu
        self._output_list = []

        # init the functions
        self.bubbleSort(input_list)
        # self.OuputList()
        self.isString = isString

    def bubbleSort(self, arr):
        n = len(arr)

        # Traverse through all array elements
        for i in range(n):

            # Last i elements are already in place
            for j in range(0, n-i-1):

                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    def stringSort(self, arr):
        alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'j', 'K', 'L',
                 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X',
                 'Y','Z']
        for j in range(0, len(arr)):
            for i in range(0, len(arr)):
                _sorted = False
                if i != len(arr)-1:
                    for k in range(0,len(arr[i])):
                        if not _sorted:
                            if k != (len(arr[i]) and len(arr[i+1])):
                                if alpha.index(arr[i][k]) > alpha.index(arr[i+1][k]):
                                    arr[i], arr[i+1] = arr[i+1], arr[i]
                                    _sorted = True
                                elif alpha.index(arr[i][k]) < alpha.index(arr[i+1][k]):
                                    _sorted = True
                                else:
                                    if len(arr[i+1]) < len(arr[i]):
                                        arr[i], arr[i+1] = arr[i+1], arr[i]
                                        _sorted = True
    def Stringconvert(self,arr):
        for j in range(0, len(arr)):
            arr[j] = arr[j].upper()


    @property
    def OuputList(self):
        arr = self.input_list
        if(self.isString):
            self.Stringconvert(arr)
            self.stringSort(arr)
            for i in range(len(arr)):
                self._output_list.append(arr[i])
            return self._output_list
        else:
            self.bubbleSort(arr)
            for i in range(len(arr)):
                self._output_list.append(arr[i])
            return self._output_list

# Driver code to test above
if __name__ == "__main__":
    arr = [1, 4, 2, 6]
    bubble = BubbleSort(arr,False)
    print(bubble.OuputList)
    # sorted = []
#
# bubbleSort(arr)
#
# print ("Sorted array is:")
# for i in range(len(arr)):
#     sorted.append(arr[i])
#     #print ("%d" %arr[i]),
#
# print(sorted)
