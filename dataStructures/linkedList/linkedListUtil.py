# linked list util module


class Node():
    """
        Creates Nodes for linked list
    """

    data = None
    next = None

    def __init__(self, data: int = 0, next=None) -> None:
        """
            initializes the Node object
        """
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f"Data: {self.data}"


# linked list util funtions

class LinkedList():

    head = None

    def add(self, data: int, begin: bool = True):
        """
            returns the head node after inserting a node in the end or begining
        """

        head = self.head

        if head is None:
            self.head = Node(data=data)

        # if data is to be inserted in the end
        if begin == False:

            while head.next is not None:
                head = head.next
                print(head.data)

            head.next = Node(data=data, next=None)

        # if the data is to be inserted in the begining
        else:
            self.head = Node(data=data, next=head)


    def addMid(self, data: int) -> Node:
        """
            adds data in the middle of the linked list
        """

        head = self.head

        # is head is none then call the add function
        if head is None:
            self.head = self.add(data=data, begin=True)

        size = 0
        newhead = head

        while head is not None:
            size += 1
            head = head.next

        # get the mid position
        size //= 2
        head = newhead

        while size > 1:

            head = head.next
            size -= 1

        newNode = Node(data, head.next)
        head.next = newNode

        self.head = newhead

    def display(self) -> None:
        """
            diplays the nodes of the linked list
        """
        
        head = self.head

        if head is None:
            print("[LinkedList-ERROR] - The List is Empty")

        else:

            while head.next is not None:
                print(head.data, "->", end=" ")
                head = head.next

            print(head.data)



    def delete(head: Node, begin: bool = True) -> Node:
        """
            returns the head node after deleting a node in the end or begining
        """

        newHead = head

        if head is not None:

            if begin:
                newHead = head.next

            else:

                while head.next.next is not None:
                    head = head.next

                head.next = None

        return newHead