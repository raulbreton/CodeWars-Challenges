"""
1. Implement Length() to count the number of nodes in a linked list.
2. Implement Count() to count the occurrences of an integer in a linked list.
"""
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(node):
    if not node: return 0
    count = 0 
    while node.next is not None:
        count += 1
        node = node.next
    count += 1
    return count
  
def count(node, data):
    if not node: return 0
    arr = []
    while node.next is not None:
        arr.append(node.data)
        node = node.next
    arr.append(node.data)
    return arr.count(data)

def run():
    v1 = Node(0)
    v2 = Node(2)
    v3 = Node(3)
    v4 = Node(2)

    v1.next = v2
    v2.next = v3
    v3.next = v4

    integer = 2

    print(length(v1), count(v1, integer))

if __name__ == "__main__":
    run()