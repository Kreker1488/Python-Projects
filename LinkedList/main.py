class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_item = Node(data)
        if (self.tail):
            self.tail.next = new_item
            if (self.size == 1):
                self.head.next = new_item
        else:
            self.head = new_item
        self.tail = new_item
        self.size += 1

    def delete(self):
        if (self.head == None):
            print('poshel nahui')
            return 0
        data = self.head.data
        self.head = self.head.next
        if (self.head == None):
            self.tail = None
        self.size -= 1
        return data

    def debug(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        print(result)

#тест очереди
'''q = Queue()
q.append(1)
q.append(2)
q.append(3)
q.debug()
print('')

q.delete()
q.debug()
print('')

q.delete()
q.debug()
print('')

q.delete()
q.debug()
print('')

q.delete()
q.debug()
print('')'''


class Dequeue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append_to_end(self, data):
        new_item = Node(data)
        if (self.head == None):
            self.head = new_item
            self.tail = new_item
        elif (self.tail):
            self.tail.next = new_item
            if (self.size == 1):
                self.head.next = new_item
        self.tail = new_item
        self.size += 1

    def append_to_start(self, data):
        new_item = Node(data)
        if (self.head == None):
            self.head = new_item
            self.tail = new_item
        elif (self.head):
            new_item.next = self.head
            self.head = new_item
        self.size += 1

    '''def delete_in_end(self):
        if (self.head == None):
            print('poshel nahui')
            return 0
        data = self.tail.data
        self.tail'''