# singly linked list

# Creating a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_data):
        node = Node(new_data)
        node.next = self.head
        self.head = node

    def append(self, new_data):
        node = Node(new_data)
        current = self.head
        if current != None:
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node
            return

    def insert(self, new_data, position):
        node = Node(new_data)
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    node.next = current.next
                    current.next = node
                current = current.next
                counter += 1
        elif position == 1:
            node.next = self.head
            self.head = node

    def get_position(self, position):
        current = self.head
        counter = 1
        if position < 1:
            return None

        if current != None:
            while current.next and counter <= position:
                counter += 1
                current = current.next
            return current
        else:
            return None

    def deleteNodeWithPosition(self, position):
        current = self.head
        previous = self.head
        counter = 0
        if self.head is None:
            return

        if position == 0:
            current = current.next
            return current

        while current is not None:
            if counter == position:
                temp = current.next
                break
            counter += 1
            previous = current
            current = current.next
        previous.next = temp
        return previous

    def deleteNodeWithKey(self, key):
        current = self.head
        if current is not None:
            if current == key:
                self.head = current.next
                return

        while current is not None:
            if current.data == key:
                break
            previous = current
            current = current.next

        if(current == None):
            return

        previous.next = current.next
        current = None

    # function to print the linked list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    # Test cases
    # Set up some Elements
    ll = Linkedlist()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)

    print(ll.get_position(3).data)
    ll.insert(23, 4)
    ll.insertAtBeginning(27)
    print('Created linked list is:')
    ll.printList()
