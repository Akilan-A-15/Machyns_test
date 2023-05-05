# 4)	Write a Linked list program.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
            
        last_node.next = new_node
        
    def prepend(self, data):
        new_node = Node(data)
        
        new_node.next = self.head
        self.head = new_node
        
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist.")
            return
        
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def delete_node(self, key):
        current_node = self.head
        
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next
            
        if current_node is None:
            return
        
        prev_node.next = current_node.next
        current_node = None
        
    def print_list(self):
        current_node = self.head
        
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
