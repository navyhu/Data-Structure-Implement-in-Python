
class PriorityQueue(object):
    def __init__(self):
        self.values = []

    def isEmpty(self):
        if len(self.values) == 0:
            return True

        return False

    def insert(self, value):
        if value == None:
            return False

        values = self.values
        values.append(value)

        index = len(values) - 1

        if index == 0:
            return True

        while index > 0 and value < values[int(index/2)]:
            values[index] = values[int(index/2)]
            values[int(index/2)] = value

            index = int(index/2)

        return True

    def deleteMin(self):
        values = self.values

        if len(values) == 0:
            return None

        if len(values) == 1:
            return values.pop(0)

        #get the element been deleted, percolate down
        deleteElement = values[0]
        index = 0
        values[0] = values.pop(len(values) - 1)

        while index*2 + 1 < len(values):
            #Find out the smaller child
            lindex = (index + 1)*2 - 1 #left child
            rindex = (index + 1)*2      #right child
            if rindex < len(values):
                if values[lindex] < values[rindex]:
                    if values[index] > values[lindex]:
                        #Switch the parent and the left child
                        current = values[index]
                        values[index] = values[lindex]
                        values[lindex] = current
                        index = lindex
                    else:
                        break
                else:
                    if values[index] > values[rindex]:
                        #Switch the parent and the right child
                        current = values[index]
                        values[index] = values[rindex]
                        values[rindex] = current
                        index = rindex
                    else:
                        break
            else:
                if values[index] > values[lindex]:
                    #switch the parent and the left child
                    current = values[index]
                    values[index] = values[lindex]
                    values[lindex] = current
                    index = lindex
                else:
                    break

        return deleteElement

    def valuest(self):
        return self.values

if __name__ == '__main__':
    values = [3, 4, 2, 0, 6, 9, 23]

    pq = PriorityQueue()
    for value in values:
        pq.insert(value)

    print(pq.valuest())
    values = pq.valuest()
    while len(pq.valuest()) > 0:
        print(pq.deleteMin())
        print(pq.valuest())

