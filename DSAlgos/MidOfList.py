from sys import path
path.insert(0, '..')

from dataStructures.linkedList.linkedListUtil import LinkedList


def validateArray(array: list = []) -> list:
    """
        validates if the array is of odd length or not.
    """

    if len(array) % 2 == 0:

        array = [str(element) for element in array]
        message = "array must be of odd length but an array of even length was provided - " + "[{}]".format(", ".join(array))

        raise ValueError()

    return array


def listToLinkedlist(array: list = [10, 20, 30, 40, 50]) -> LinkedList.head:
    """
        given the array of elements this function returns the head of the linked list formed from those elements in the same order.
    """

    # creating the LinkedList object
    linkedList = LinkedList(array)

    return linkedList.head


def getMiddleElement(start: LinkedList.head) -> int:
    """
        given the head of the linked list this function returns the middle element of the linkedlist. |
        two pointers sloth and rabbit both points initially to the same node but the rabbit pointer travese two times the speed of 
        the sloth pointer.
    """ 
    sloth = rabbit = start

    while rabbit is not None and rabbit.next is not None:
        
        sloth = sloth.next
        rabbit = rabbit.next

        if rabbit != None:
            rabbit = rabbit.next

    return sloth.data

if __name__ == "__main__":
    array = validateArray([10, 20, 60, 40, 50])
    start = listToLinkedlist(array)
    print(getMiddleElement(start))
    array = validateArray([40, 20, 10, 40])
    start = listToLinkedlist(array)
    print(getMiddleElement(start))