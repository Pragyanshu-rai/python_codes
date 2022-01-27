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

    def __init__(self, array: list = [], reverse = False) -> None:
        """
            initializes the LinkedList object
        """

        if reverse: 
            array = array[::-1]

        for data in array:
            self.add(data, False)


    def add(self, data: int, begin: bool = True) -> Node:
        """
            returns the head node after inserting a node in the end or begining depending on the begin flag
        """

        head = self.head

        if head is None:
            self.head = Node(data=data)
            return self.head
        
        # if data is to be inserted in the end
        if begin == False:

            while head.next is not None:
                head = head.next

            head.next = Node(data=data, next=None)

        # if the data is to be inserted in the begining
        else:
            head = head.next
            head = Node(data=data, next=head)
        
        return self.head


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

        return self.head


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


    def delete(self, begin: bool = True) -> Node:
        """
            returns the head node after deleting a node in the end or begining
        """

        newHead = self.head

        if self.head is not None:

            if begin:
                self.head = newHead.next

            else:

                while newHead.next.next is not None:
                    newHead = newHead.next

                newHead.next = None

        return self.head


if __name__ == "__main__":

    ll = LinkedList([10, 20, 30, 40, 50])
    ll.display()