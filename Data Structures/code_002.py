
class Node:
    def __init__(self):
        self.data=None
        self.next=None
    
    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next=next

class LinkedList:
    
    def __init__(self, head):
        self.head=head
    
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current=self.head
        count=0
        while current:
            count+=1
            current=current.getNext()
        return count
    
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        