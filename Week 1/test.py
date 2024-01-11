from DoublyLinkedList import DoublyLinkedList

dll1 = DoublyLinkedList("customer1")
dll1.insert_at_back("customer2")
dll1.insert_at_back("customer3")
dll1.print_val_backward()
dll1.remove("customer2")
dll1.print_val_backward()