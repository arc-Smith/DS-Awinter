class DoublyNode: # (done)
    # INITIALIZER (done)
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        
    # GETTERS (done)
    def get_value(self):
        return self.val
    def get_next(self):
        return self.next
    def get_prev(self):
        return self.prev
    
    # SETTERS (done)
    def set_value(self, val):
        self.val = val
    def set_next(self, next):
        self.next = next
    def set_prev(self, prev):
        self.prev = prev

class DoublyLinkedList:
    # INITIALIZER (done)
    def __init__(self, val):
        headNode = DoublyNode(val)
        self.head = headNode # this ALWAYS points at the first node of the LinkedList
        self.tail = self.head

    # GETTER (done)
    def get_head_node(self):
        return self.head
    def get_tail_node(self):
        return self.tail

    # Method to insert a new node to the front of the LinkedList (done)
    def insert_at_front(self, newVal):
        # Step 1: create the new node (done)
        newNode = DoublyNode(newVal)

        # Step 2: replace head's previous with new node (done)
        self.head.prev = newNode

        # Step 3: new node's next points to self.head (done)
        newNode.next = self.head

        # Step 4: update self.head (done)
        self.head = newNode
        

    # Method to print all the values inside of the LinkedList
    def print_val_backward(self):
        # Step 1: initialize return variable
        newString = ""

        # Step 2: initialize temporary pointer at the tail
        current = self.tail

        # Step 3: append the current.val to the string
        newString += str(current.val) + "->"

        while current.prev != None:
            current = current.prev
            # Step 4: go to previous
            newString += str(current.val) + "->"

        # Step 5: printing string
        print(newString + "None")


    def insert_at_back(self, newVal):
        newNode = DoublyNode(newVal)
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode

    def insert(self, newVal, location):
        pass
    
    def remove(self, removeVal):
        # no node to remove
        if self.head == None:
            print("empty linked list")
            return
        # one node in linked list that's removed
        elif current.val == removeVal and not self.head.prev and not self.head.next:
            self.head = None
            self.tail = None
            return
        # head node is removed
        elif self.head.val == removeVal:
            self.head = self.head.next
            self.head.prev = None
            return
        # tail node is removed
        elif self.tail.val == removeVal:
            self.tail = self.tail.prev
            self.tail.next = None

        # removing a node in the middle
        # Step 1: create temporary pointer
        current = self.head
        # Step 2: parse through each node and compare the node's vals
        while current != None:
            if current.val == removeVal:
                # Step 3: current's previous node is updated
                current.prev.next = current.next
                # Step 4: current's next node is updated
                current.next.prev = current.prev
                print("Node has been removed")
                return
            else:
                current = current.next
        print(f"{removeVal} is not in the Linked List")

    def findIndex(self, targetVal):
        # Step 1: create our return variable
        index = 0

        # Step 2: create our temporary variable
        current = self.head

        # Step 3: looping till we possibly find targetVal
        while current != None:
            if current.val == targetValue:
                return index
            else:
                index += 1
                current = current.next

        # Step 4: returning
        return None # indicates that targetVal is NOT inside of the linked list