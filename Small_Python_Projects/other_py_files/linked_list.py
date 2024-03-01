# Attempt at creating Python Linked List

class Node():
    """ This class simply creates a node, which contains a data value and a next value"""
    def __init__(self, dataval=None):
        self.dataval = dataval
        # This attrib is set to None initially because another node hasn't been created yet.
        self.nextval = None

class SLinkedList():
    """Singularly linked list"""

    def __init__(self):
        self.headval = None
    
    def print_list(self):
        # Initially assign the head value as the print value.
        printval = self.headval
        # check to make sure that the value is not None.
        while printval is not None:
            # Print that nodes value.
            print(printval.dataval)
            # As you iterate reassign the printvalue to the next node. 
            # In this instance it would be "Sun" -> "Mon" -> "Tue"
            printval = printval.nextval

    def at_beginning(self, new_data):
        NewNode = Node(new_data)
        # Update the new nodes next value to the already existing head.
        NewNode.nextval = self.headval
        # Now assign the NewNode as the new head.
        self.headval = NewNode
    
    def at_end(self, new_data):
        NewNode = Node(new_data)
        # If there is no headval then this new node becomes the head.
        if self.headval = None:
            self.headval = NewNode
            print("No head value found, Updated with new node.")
        # Iterate through the linked list until there is no nextval.
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode


# Create an instance of SLinkedList()
list1 = SLinkedList()
# Assign the value "Sun" to list1 headvalue
list1.headval = Node("Sun")
# Create the next 2 Nodes
d2 = Node("Mon")
d3 = Node("Tue")
# Link first node to second node.
list1.headval.nextval = d2
# Link the second to the third node.
d2.nextval = d3
list1.at_beginning("Sat")
# If we wanted to add a new head value at the beginning of the list this can be done with a function.
# Adding a value at the end...
list1.at_end("Wed")