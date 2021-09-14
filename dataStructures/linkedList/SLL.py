from linkedListUtil import LinkedList


ll = LinkedList()

ll.add(23)
ll.add(69, False)

ll.addMid(22)

ll.display()

ll.addMid(67)

ll.display()


def inorder(root):

    if root is None:
        return 
    
    inorder(root.left);
    print(root.val)
    inorder(root.right)