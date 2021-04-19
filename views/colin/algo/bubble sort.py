# Python program for implementation of Bubble Sort

def bubbleSort(arr):
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

class BubbleSort:
    def __init__(self, input_list):

        # init/declare the variables
        self.input_list = input_list


        # init the outpu
        self._output_list = []

        # init the functions
        self.bubbleSort(arr)
        self.OutputList()

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
        @property
        def OuputList(self):
            arr = self.input_list
            bubbleSort(arr)
            return self._output_list

# Driver code to test above
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted = []

    bubbleSort(arr)

    print ("Sorted array is:")
    for i in range(len(arr)):
        sorted.append(arr[i])
        #print ("%d" %arr[i]),

    print(sorted)
