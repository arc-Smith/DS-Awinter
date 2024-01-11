class SinglyNode:
    # INITIALIZER
    def __init__(self, val, next=None): # O(1) time
        self.val = val # O(1) time
        self.next = next # O(1) time
        
    # GETTERS
    def get_value(self): # O(1) time
        return self.val # O(1) time
    def get_next(self): # O(1) time
        return self.next # O(1) time
    
    # SETTERS
    def set_value(self, val): # O(1) time
        self.val = val # O(1) time
    def set_next(self, next): # O(1) time
        self.next = next # O(1) time

class SinglyLinkedList:
    # INITIALIZER
    def __init__(self, val): # O(1) time
        self.head = SinglyNode(val) # this ALWAYS points at the first node of the LinkedList | O(1) time

    # GETTER
    def get_head_node(self): # O(1) time
        return self.head # O(1) time
    
    def insert(self):
        pass

    # Method to insert a new node to the front of the LinkedList
    def insert_at_front(self, newVal): # O(1) time
        # Step 1: knowing the value to put at the front
        # newVal input provides that above

        # Step 2: creating the node to house that value
        newNode = SinglyNode(newVal) # self.val = 9 | O(1) time

        # Step 3: creating the connection 
        # -updating the self.next
        newNode.next = self.head # O(1) time

        # Step 4: update the self.head because the new value entered is the new head
        # -updating the self.head of the LinkedList
        self.head = newNode # O(1) time
    
    # Method to print all the values inside of the LinkedList
    def print_val(self): # O(n) time
        result = "" # O(1) time

        # Step 1: create a temporary pointer (it's a copy of the self.head)
        current = self.head # current is a Node | O(1) time

        # Step 2: loop through the LinkedList 
        # -we use a while loop
        while current != None: # the while loop is asking if we are pointing to a Node (NOT providing movement) | O(n) time

            # Step 3: put those values inside of the string
            result += (str(current.val) + "->") # result += "9->" | O(1) time

            # Step 4: we want to move our pointer
            current = current.next # O(1) time
            # current starts Node(9)  
            # current.next is initially Node(10)

        return result + "None" # O(1) time

    def insert_at_back(self, newVal): # O(n) time
        # Step 1: Create the Node that we want to add
        newNode = SinglyNode(newVal) # O(1) time

        # Step 2 setup temporary pointer
        current = self.head # O(1) time

        # Step 3: Loop to the last Node
        while current.next != None: # O(n) time
            # Step 4: move cursor
            current = current.next # O(1) time
        # current by the end points to the last node

        # Step 5: adding in the new node
        current.next = newNode # O(1) time

    def insert(self, valToEnter, index):
        # Step 1a: get the length of the linked list
        length = 0
        # Step 1b: setup temporary pointer
        current = self.head
        # Step 1c: looping through linked list
        while current != None:
            # Step 1d: increment the length
            length += 1
            # Step 1e: move/shift the current pointer
            current = current.next
        
        # Step 2: insertion at back of linked list
        if index >= length:
            self.insert_at_back(valToEnter)
        # Step 3: insertion at front of linked list
        elif index == 0:
            self.insert_at_front(valToEnter)
        # Step 4: insertion at middle of linked list
        else:
            self.insert_at_middle(valToEnter)
        
    def insert_at_middle(self, newVal):
        # Step 1: Create new node
        newNode = SinglyNode(valToEnter)

        # Step 2: setup the temporary pointer
        current = self.head

        # Step 3: looping till the current's next should be our new node
        while index != 1:
            # Step 4: decrement index
            index -= 1
            # Step 5: move/shift current pointer
            current = current.next
        
        # Step 6: establishing connections
        newNode.next = current.next #Node3->Node4
        current.next = newNode #Node2->Node3
        
    def findIndex(self, targetValue):
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

    def remove1(self, valToRemove):
        if self.head.val == valToRemove:
            self.head = self.head.next
        current = self.head
        while current.next != None:
            if valToRemove == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        
    # def remove2(self, valToRemove):
    #     # Step 1: setup dummy node
    #     dummyNode = SinglyNode(0, self.head)

    #     # Step 2: setup prev & current pointers
    #     prev = dummyNode
    #     current = self.head

    #     # Step 3: keep looping until current points at the Node with value to be removed
    #     while current != None:
    #         if current.val == valToRemove:
    #             prev.next = prev.next.next # DummyNode->Node2
    #         else:
    #             current = current.next
    #             prev = prev.next
        
    #     self.head = dummyNode.next

# def insert(self, newVal, location): # O(n) time
#     # Step 1: get the length of the linked list
#     length = 0 # O(1) time
#     current = self.head # O(1) time
#     while current: # O(n) time
#         length += 1 # O(1) time
#         current = current.next # O(1) time
    
#     # Step 2: handle insertion at the back
#     if location > length: # O(1) time
#         self.insert_at_back(newVal) # O(n) time
#     # Step 3: handle insertion at the front
#     elif location == 0: # O(1) time
#         self.insert_at_front(newVal) # O(n) time
#     # Step 4: handle insertion in the middle somewhere
#     else:
#         # Step 1 (for middle insertion): Create the new node
#         newNode = Node(newVal) # O(1) time

#         # Step 2 (for middle insertion): Setup temporary pointer
#         current = self.head # O(1) time

#         # Step 3 (for middle insertion): Loop through linked list
#         while location != 1: # O(n) time
#             # Step 4 (for middle insertion): Updating location and temporary pointer
#             location -= 1 # O(1) time
#             current = current.next # O(1) time
        
#         # Step 5 (for middle insertion): Update next for new node and current node (in that specific order or else you lose the connection)
#         newNode.next = current.next # O(1) time
#         current.next = newNode # O(1) time

# def findIndex(self, targetVal): # O(n) time
#     # Step 1: setup return variable (in this case it's named index)
#     index = 0 # O(1) time

#     # Step 2: setup temporary pointer
#     current = self.head # O(1) time

#     # Step 3: loop through linked list
#     while current: # O(n) time
#         # Step 4: check if we've reached target
#         if current.val == targetVal: # O(1) time
#             break # O(1) time
#         # Step 5: update index and temporary pointer
#         else:
#             index += 1 # O(1) time
#             current = current.next # O(1) time
    
#     # Step 6: return index
#     print(f"Node is located at index={index}") # O(1) time
#     return index # O(1) time

# def remove(self, removeVal): # O(n) time
#     # Step 1: setup dummy node
#     dummyNode = SinglyNode(0, self.head) # O(1) time

#     # Step 2: setup temporary node
#     current = dummyNode # O(1) time

#     # Step 3: loop through linked list
#     while current: # O(n) time
#         # Step 4: put break condition
#         if current.next.val == removeVal: # O(1) time
#             break
#         # Step 5: move temporary pointer
#         else:
#             current = current.next # O(1) time
    
#     # Step 6: remove the node we no longer want
#     current.next = current.next.next # O(1) time