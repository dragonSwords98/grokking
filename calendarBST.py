# Contributed by: Bryan Ling


# constraints
# 0 <= start < end <= 109
# At most 1000 calls will be made to book.

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Inorder traversal
    # Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res = res + self.inorderTraversal(root.right)
        return res

class MyCalendar:
    bookings = None

    def __init__(self):
        self.bookings = TreeNode()
        
    def book(self, start:int, end:int) -> bool:
        if self.bookings.val:
            return self.bookCalendar(start, end, self.bookings)
        else:
            self.bookings.val = [start, end]
            return True

    def bookCalendar(self, start: int, end: int, tree: TreeNode) -> bool:
        if start == tree.val[0]:
            # double booked with this event
            return False
        elif start >= tree.val[0]:
            if start < tree.val[1]:
                # double booked with this node
                return False
            elif tree.right:
                # continue traversing for conflicts
                return self.bookCalendar(start, end, tree.right)
            else:
                # space available after node, event is booked
                tree.right = TreeNode([start, end], None, None)
                return True
        elif end > tree.val[0]:
            # double booked with this node
            return False
        else:
            if tree.left:
                # continue traversing for conflicts
                return self.bookCalendar(start, end, tree.left)
            else:
                # space available after node, event is booked
                tree.left = TreeNode([start, end], None, None)
                return True

                

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

def runCalendarTest(input: list[int], expected: list[bool]) -> bool:
    obj = MyCalendar()
    results = []
    for i in input:
        results.append(obj.book(*i))
    
    print(results, expected)
    assert results == expected



runCalendarTest(
    [[37,50],[33,50],[4,17],[35,48],[8,25]],
    [True,False,True,False,False],
)
runCalendarTest(
    [[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]],
    [True, True, False, False, True, False,True, True, True, False],
)


