import random

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
    
if __name__ == '__main__':
    #values = [3, 4, 2, 6, 78, 21, 0, 32, 79]

    
    sort = Sort()
    values = sort.randomValues(20)
    print(values)
    #sort.insertionSort(values)
    sort.shellSort(values)

    print(values)
