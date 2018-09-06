class Node():
    def __init__(self, val):
        self.val = val
        self.previous = None 
        self.next = None 

    def traverse(self):
        node = self 
        while node is not None:
            print(node.val)
            node = node.next

    def traverse_backwards(self):
    	node = self 
    	while node is not None:
    		print(node.val)
    		node = node.previous

    def remove_duplicates(self):
    	node = self 
    	unique = []
    	previous = None
    	while node is not None:
    		if node.val in unique:
    			previous.next = node.next 
    		else:
    			unique.append(node.val)
    		previous = node 
    		node = node.next 


d1 = Node('Monday')
d2 = Node('Tuesday')
d3 = Node('Wednesday')
d4 = Node('Thursday')
d5 = Node('Friday')
d6 = Node('Saturday')
d7 = Node('Sunday')
d8 = Node('Sunday')

d1.next = d2 
d2.previous = d1 
d2.next = d3 
d3.previous = d2 
d3.next = d4
d4.previous = d3 
d4.next = d5 
d5.previous = d4
d5.next = d6
d6.previous = d5
d6.next = d7
d7.previous = d6 
d7.next = d8 
d8.previous = d7


d1.remove_duplicates()
d1.traverse()
