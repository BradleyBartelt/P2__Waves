class BubbleSortString:
    def __init__(self, input_list):

        # init/declare the variables
        self.input_list = input_list


        # init the output
        self._output_list = []
        self._output_list_len = []
        self._output_list_final = []
        # init the functions
        self.organizeList(input_list)
        self.bubbleSort(self._output_list_len, self._output_list)
        # self.replacing()

    def organizeList(self, arr):
        n = len(arr)

        #self._output_list.append('starting append')
        # Traverse through all array elements
        for i in range(n):
            self._output_list.append(arr[i]) # appending the original list
            self._output_list_len.append(len(arr[i])) # appending the lnehgt of each string

    def bubbleSort(self, arr, second):
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
                    second[j], second[j+1] = second[j+1], second[j]

    @property
    def OuputList(self):
        return self._output_list

    @property
    def OuputListLen(self):
        return self._output_list_len

    #@property
    #def OuputListFinal(self):
    #    return self._output_list_final

# Driver code to test above
if __name__ == "__main__":
    arr = ['dog', 'fart', 'testing', 'today', 'nine', 'sixty', 'two-hundred']
    bubble = BubbleSortString(arr)
    print(bubble.OuputList)
    #print('final list' +str(bubble.OuputListFinal))

