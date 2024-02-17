class Node:
    """
    An object for storing a single node of a linked list.
    Models teo attributes - data and the link to the next node in the linked list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data= data

    def __repr__(self):
        return "<Node data: %s>" % self.data
    
class LinkedList:
    """
    singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        return the number of nodes in the lists takes O(n) time """
        current = self.head
        count = 0
        
        while current:
            count +=1
            current = current.next_node

        return count
    def add(self,data):
        """
        it adds a new node containing `data` at the head of  the list Takes O(1) time"""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self,key):
        """
        search  for the first node containing data that matches the key
        Returns the node or None  if not found
        Take O(n) time
        """
        current = self.head
        while current:
            if current.data==key:
                return current
            else:
                current =current.next_node
        return None
    
    def insert(self,data,index):

        """"
        INsert a new node containing data at index position
         insertion takes constant time  nut  finding the node at the insertion point 
         takes O(n)

         takes overall

        """
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)
            
            position = index
            current = self.head

            while position  > 1:
                current = Node.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self,key):

        """
        removes a node  containing data that matches the key
        returns the node and none if the key does not exist
         take O(n) timw
        """
        current = self.head
        previous= None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data ==key :
                found = True
                previous.next_node = current.next_node
            else:
                previous =current
                current = current.next_node
        return current



    def __repr__(self):
        """
        Return a string representation of the list takes O(n)
        """
        nodes = []
        current= self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]"% current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]"% current.data)
            
            current =current.next_node
        return '-> '.join(nodes)


