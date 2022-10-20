from linked_list import *
from linked_list_completed import *

print("\n\n")
print("--------------------Linked List (linkedList.py)--------------------")
print("\n\n")
# Create a new linked list
linkedList1 = SLinkedList()
# Append some values
linkedList1.append(5)
linkedList1.append(6)
linkedList1.append(8)
# print linked list
linkedList1.listPrint()
# prepend to the linked list
linkedList1.prepend(4)
# print linked list again
linkedList1.listPrint()
# Insert between a linked list
linkedList1.insertBetween(4,7)
# print linked list again
linkedList1.listPrint()
# delete first node
linkedList1.removeFirstNode()
# print linked list again
linkedList1.listPrint()
# Remove a node with a key
linkedList1.removeKeyElement(6)
# print linked list again
linkedList1.listPrint()
#Try to remove a node that does not exist
linkedList1.removeKeyElement(25)