## Doubly Linked Lists
## Anas Zughayyar

class DLNode:
    def __init__(self, value):
        self.prev = None
        self.data = value
        self.next = None

class DList:
    def __init__(self):
        self.head = None
    
    def print_values(self):
        runner = self.head
        counter = 0
        while runner is not None:
            print(counter," : ",runner.prev, " > ", runner.value, " > ", runner.next.value)
            runner = runner.next
            counter += 1
        return self 
