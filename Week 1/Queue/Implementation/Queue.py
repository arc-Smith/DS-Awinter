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

class Queue:
    def __init__(self, max, nodeVal) -> None:
        node = DoublyNode(nodeVal)
        self.front = node
        self.back = node
        self.max = max
        self.size = 1
    
    def is_empty(self) -> bool:
        if self.size < 1:
            print("Queue is empty")
            return True
        else:
            return False










# from node import Node

# class Queue:
#   def __init__(self, max_size=None):
#     self.head = None
#     self.tail = None
#     self.max_size = max_size
#     self.size = 0
    
#   def enqueue(self, value):
#     if self.has_space():
#       item_to_add = Node(value)
#       print("Adding " + str(item_to_add.get_value()) + " to the queue!")
#       if self.is_empty():
#         self.head = item_to_add
#         self.tail = item_to_add
#       else:
#         self.tail.set_next_node(item_to_add)
#         self.tail = item_to_add
#       self.size += 1
#     else:
#       print("Sorry, no more room!")
         
#   def dequeue(self):
#     if self.get_size() > 0:
#       item_to_remove = self.head
#       print(str(item_to_remove.get_value()) + " is served!")
#       if self.get_size() == 1:
#         self.head = None
#         self.tail = None
#       else:
#         self.head = self.head.get_next_node()
#       self.size -= 1
#       return item_to_remove.get_value()
#     else:
#       print("The queue is totally empty!")
  
#   def peek(self):
#     if self.size > 0:
#       return self.head.get_value()
#     else:
#       print("No orders waiting!")
  
#   def get_size(self):
#     return self.size
  
#   def has_space(self):
#     if self.max_size == None:
#       return True
#     else:
#       return self.max_size > self.get_size()
    
#   def is_empty(self):
#     return self.size == 0