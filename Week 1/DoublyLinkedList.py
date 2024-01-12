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
        print("inside of remove")
        current = self.head
        if current.val == removeVal:
            self.head = current.next
            self.head.prev = None
            return

        if self.tail.val == removeVal:
            self.tail = self.tail.prev
            self.tail.next = None
            return 
        
        while current != None:
            
            if current.val != removeVal:
                current = current.next
                return

            else:
                    print(current.val)
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    return
                

    def findIndex(self, targetVal):
        pass