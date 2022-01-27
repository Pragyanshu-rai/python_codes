from .linkedListUtil import Node, LinkedList

message = """Hey there! Welcome to singleLinkedList please select an action to be performed on the linked list
1. Insert
2. Delete
3. Display
4. Exit
5. Mid
>> """

insert="Insert in the begning? [y/n] "
remove="Delete from the begning? [y/n] "


def startList(interactive: bool = True) -> Node:
    """
        starts the prompting the user of actions to be performed on the linked list and displays the results if interactive is set to true.
    """

    head = None

    while True:

        response = input(message)

        if response == '5' and interactive:
            data = int(input("Enter The Data: "))
            head = addMid(head, data=data)

        if response == '4':
            if interactive : print("Bye..")
            break;
        
        if response == '3' and interactive:
            display(head)
        
        if response == '2':
            begin = input(remove) == 'y'
            head = delete(head, begin)
            
            if head is not None and interactive:
                print("data deleted")

        if response == '1':
            begin = input(insert) == 'y'
            data = int(input("Enter The Data: "))
            head = add(head, data, begin)
            if interactive : print("data inserted")
    
    return head


if __name__ == "__main__":
    startList()