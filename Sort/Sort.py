import random

class Sort(object):
    def swap(self, value1, value2):
        tmp = value1
        value1 = value2
        value2 = tmp

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

    def randomValues(self, count):
        values = []
        for i in range(0, count):
            value = random.randint(0, count*10)
            values.append(value)

        return values

if __name__ == '__main__':
    #values = [3, 4, 2, 6, 78, 21, 0, 32, 79]

    
    sort = Sort()
    values = sort.randomValues(500)
    print(values)
    sort.insertionSort(values)

    print(values)
