# Copied Code:
# class Node:
#   def __init__(self, value, link_node=None):
#     self.value = value
#     self.link_node = link_node
    
#   def set_link_node(self, link_node):
#     self.link_node = link_node
    
#   def get_link_node(self):
#     return self.link_node
  
#   def get_value(self):
#     return self.value

# Node a: val=2, next=None
# b = Node(3)
# a, b
# a.set_next(b)
# a.next = None

# INITIALIZATION: a = Node(2)
    # SETTER: a.set_next(b)
    # GETTER: a.get_next()

    # b.addMeAndNext()
    # a.addMeAndNext()

class Node:
    def __init__(self, val, nxt=None): # O(1) time
        self.value = val # O(1) time
        self.next = nxt # O(1) time
    
    def set_next(self, nxt): # O(1) time
        self.next = nxt # O(1) time
    
    def set_val(self, val): # O(1) time
        self.value = val # O(1) time

    def get_next(self): # O(1) time
        return self.next # O(1) time

    def get_val(self): # O(1) time
        return self.value # O(1) time

    def addMeAndNext(self): # O(1) time
        return self.value + self.next.value # O(1) time

a = Node(66) # O(1) time
b = Node(3) # O(1) time
a.set_next(b) # O(1) time
print(a.get_val()) # O(1) time
a.set_val(33) # O(1) time
print(a.get_val()) # O(1) time
print(a.addMeAndNext()) # O(1) time