
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

        #get the element been deleted
        deleteElement = values[0]

        #Percolate up, fill the root with it's child(eventually with the last
        # node
        index = len(values) - 1

        if index == 0:
            values.pop(index)
            return deleteElement

        current = values[index]
        parent = values[int(index/2)]

        while index > 0:
            parent = values[int(index/2)]
            values[int(index/2)] = current
            index = int(index/2)

            current = parent

        #remove the last element
        values.pop(index)

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

