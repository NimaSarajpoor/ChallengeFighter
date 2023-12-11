# link: https://leetcode.com/problems/add-two-numbers/description/

class ListNode:
     def __init__(self, val, next=None):
         self.val = val
         self.next = next

    # alternatively, we may use dictionary!


def convert_linkedlist_to_list(root):
    node = root
    out = []
    while node is not None:
        out.append(node.val)
        node = node.next
    return out


def convert_list_to_linkedlist(lst):
    root = ListNode(lst[0])
    node = root
    for val in lst[1:]:
        node.next = ListNode(val)
        node = node.next
    
    return root

def naive_add_two_numbers(root_A, root_B):
    """
    root_A and root_B are the root nodes of linked list A and B, respectively.
    """
    A = convert_linkedlist_to_list(root_A)
    B = convert_linkedlist_to_list(root_B)

    A = ''.join([str(x) for x in A[::-1]])
    if A == '':
        A = 0
    else:
        A = int(A)
    
    B = ''.join([str(x) for x in B[::-1]])
    if B == '':
        B = 0
    else:
        B = int(B)

    total = A + B
    out = [int(x) for x in list(str(total))[::-1]]
    root = convert_list_to_linkedlist(out)

    return root


def add_two_numbers(root_A, root_B):
    
    node_A = root_A
    node_B = root_B

    dummynode = ListNode(val=None)
    node = dummynode
    carry_over = 0
    while node_A is not None or node_B is not None:
        
        #node_A = node_A.next
        #node_B = node_B.next

        if node_A is None:
            val_A = 0
        else:
            val_A = node_A.val
            node_A = node_A.next
        
        if node_B is None:
            val_B = 0
        else:
            val_B = node_B.val
            node_B = node_B.next
        
        total = val_A + val_B + carry_over
        carry_over = total // 10
        val = total % 10
        node.next = ListNode(val)    
        node = node.next

    if carry_over > 0:
        node.next = ListNode(carry_over)

    root = dummynode.next

    return root