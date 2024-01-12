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

class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.top = None
        self.size = 0
        


















# // public class Stack {
# //   LinkedList linkedList;

# //   public Stack() {
# //     linkedList = new LinkedList();
# //   }

# //   // Push method
# //   public void push(int value) {
# //     linkedList.insertInLinkedList(value, 0);
# //     System.out.println("Inserted " + value + " in Stack");
# //   }

# //   // isEmpty
# //   public boolean isEmpty() {
# //     if (linkedList.head == null) {
# //       return true;
# //     } else {
# //       return false;
# //     }
# //   }

# //   // Pop method
# //   public int pop() {
# //     int result = -1;
# //     if (isEmpty()) {
# //       System.out.println("The Stack is Empty!");
# //     } else {
# //       result = linkedList.head.value;
# //       linkedList.deletionOfNode(0);
# //     }
# //     return result;
# //   }

# //   // Peek Method
# //   public int peek() {
# //     if (isEmpty()) {
# //       System.out.println("The Stack is Empty!");
# //       return -1;
# //     } else {
# //       return linkedList.head.value;
# //     }
# //   }

# //   // Delete Method
# //   public void deleteStack() {
# //     linkedList.head = null;
# //     System.out.println("The Stack is deleted");
# //   }
# // }
