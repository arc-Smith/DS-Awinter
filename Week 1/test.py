from SinglyLinkedList import SinglyLinkedList
from SinglyLinkedList import SinglyNode
from DoublyLinkedList import DoublyLinkedList
from DoublyLinkedList import DoublyNode

LL1 = DoublyLinkedList("Boruto")
LL1.insert_at_front("Naruto: Shippuden")
LL1.insert_at_front("Naruto")
LL1.print_val_backward()

# print(LL1.print_val())
# LL1.remove1("Neji")
# print(LL1.print_val())

# print(LL1.print_val())
# LL1.insert("Sasuke", 1)
# LL1.insert("Sakura", 1)
# print(LL1.print_val())

# print(LL1.findIndex("Madara Uchiha"))



# LL1.head.set_next(SinglyNode(10)) # we use Node(10) here because we are attaching Nodes to one another. Like a subway/train with multiple carts.
# LL1.head.next.set_next(SinglyNode(11))
# LL1.head.next.next.set_next(SinglyNode(12))

# print(LL1.val) this doesn't actually print 9 because remember that the SinglyLinkedList has no variable self.val (but the Node itself does)
# print(LL1) # returns address of SinglyLinkedList in memory
# print(LL1.head) # returns address of first Node of SinglyLinkedList
# print(LL1.head.val) # returns value of the first Node of SinglyLinkedList
# print(LL1.head.next) # returns address of second Node of SinglyLinkedList

######################################## SHOWCASE DURING CLASS ########################################
######################################## SHOWCASE DURING CLASS ########################################
######################################## SHOWCASE DURING CLASS ########################################
# LL1.insert(10, 100)
# LL1.insert(11, 100)
# LL1.insert(12, 100)
# LL1.insert(13, 100)
# print(LL1.print_val())
# print(LL1.search(13))
# LL1.findIndex(9)
# print(LL1.print_val())
# LL1.remove(12)
# print(LL1.print_val())