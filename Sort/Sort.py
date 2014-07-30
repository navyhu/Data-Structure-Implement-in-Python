import random

class HeapSort(object):
    def __init__(self):
        self.values = []

    def insert(self, value):
        values = self.values
        values.append(value)

        if len(values) == 1:
            return True

        index = len(values) - 1
        while index > 0:
            parent = int(index/2)
            if values[index] > values[parent]:
                tmp = values[parent]
                values[parent] = values[index]
                values[index] = tmp
                index = parent
            else:
                break

    def buildHeap(self, values):
        for value in values:
            self.insert(value)
        print(self.values)

    def sort(self):
        values = self.values
        for index in range(len(values) - 1, 0, -1):
            #Switch the 1st and last item
            tmp = values[0]
            values[0] = values[index]
            values[index] = tmp
            #Recover the heap
            current = 0
            while current < index:
                lindex = current*2 + 1
                rindex = current*2 + 2
                if lindex < index:
                    if rindex < index:
                        #Switch the bigger one with the parent
                        if values[lindex] > values[rindex]:
                            if values[current] < values[lindex]:
                                tmp = values[current]
                                values[current] = values[lindex]
                                values[lindex] = tmp
                                current = lindex
                            else:
                                break
                        else:
                            if values[current] < values[rindex]:
                                tmp = values[current]
                                values[current] = values[rindex]
                                values[rindex] = tmp
                                current = rindex
                            else:
                                break
                    else:
                        #Only left child exists
                        if values[current] < values[lindex]:
                            tmp = values[current]
                            values[current] = values[lindex]
                            values[lindex] = tmp
                            current = lindex
                        else:
                            break
                else:
                    break

class Sort(object):
    def randomValues(self, count):
        values = []
        for i in range(0, count):
            value = random.randint(0, count*10)
            values.append(value)

        return values

    def insertionSort(self, values):
        count = len(values)

        for i in range(0, count):
            for j in (range(i, 0, -1)):
                if values[j] < values[j - 1]:
                    #self.swap(values[i], values[i - 1])
                    tmp = values[j - 1]
                    values[j - 1] = values[j]
                    values[j] = tmp
                else:
                    break
    
    def shellSort(self, values):
        count = len(values)
        increment = int(count/2)

        while increment > 0:
            for i in range(increment, count):
                for j in range(i, increment - 1, -increment):
                    if values[j] < values[j - increment]:
                        tmp = values[j - increment]
                        values[j - increment] = values[j]
                        values[j] = tmp
                    else:
                        break

            increment = int(increment/2)

    def heapSort(self, values):
        heapsort = HeapSort()
        heapsort.buildHeap(values)
        #print(values)
        heapsort.sort()
        print(heapsort.values)

    def _mSort(self, values):
        if len(values) <= 1:
            return values
        
        halflen = int(len(values)/2)
        values1 = values[0:halflen]
        values2 = values[halflen:len(values)]
        
        values1 = self._mSort(values1)
        values2 = self._mSort(values2)
        sortedValues = []

        #merge
        index1 = index2 = 0
        while index1 < len(values1) and index2 < len(values2):
            if values1[index1] < values2[index2]:
                sortedValues.append(values1[index1])
                index1 = index1 + 1
            else:
                sortedValues.append(values2[index2])
                index2 = index2 + 1

        if index1 < len(values1):
            for value in values1[index1:len(values1)]:
                sortedValues.append(value)
        elif index2 < len(values2):
            for value in values2[index2:len(values2)]:
                sortedValues.append(value)

        return sortedValues


    def mergeSort(self, values):
        if len(values) != 0:
            return self._mSort(values)

        return values

    def _quickSort(self, values):
        length = len(values)

        if length <= 1:
            return True
        elif length == 2:
            if values[0] > values[1]:
                tmp = values[0]
                values[0] = values[1]
                values[1] = tmp
            return True

        #Find the pivot
        midIndex = int(length/2)
        if values[0] > values[-1]:
            tmp = values[0]
            values[0] = values[-1]
            values[-1] = tmp

        if values[0] > values[midIndex]:
            tmp = values[0]
            values[0] = values[midIndex]
            values[midIndex] = tmp

        if values[-1] > values[midIndex]:
            tmp = values[-1]
            values[-1] = values[midIndex]
            values[midIndex] = tmp

        pivot = values[-1]

        #Start to divide
        i = 0
        j = length - 2

        while i <= j:
            if values[i] > pivot:
                while i <= j:
                    if values[j] < pivot:
                        tmp = values[i]
                        values[i] = values[j]
                        values[j] = tmp
                        i = i + 1
                        j = j - 1
                        break
                    else:
                        j = j - 1
            else:
                i = i + 1

        values[length - 1] = values[i]
        values[i] = pivot

        values1 = values[0: i]
        values2 = values[i:]

        self._quickSort(values1)
        self._quickSort(values2)
        values[0:i] = values1
        values[i:] = values2

    def quickSort(self, values):
        if len(values) != 0:
            self._quickSort(values)
    
if __name__ == '__main__':
    #values = [3, 4, 2, 6, 78, 21, 0, 32, 79]

    
    sort = Sort()
    values = sort.randomValues(5000)
    print(values)
    #sort.insertionSort(values)
    #sort.shellSort(values)
    #sort.heapSort(values)
    #values = sort.mergeSort(values)
    sort.quickSort(values)

    print(values)
