class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head):
        if not head or not head.next:
            return None

        slow = head
        fast = head

        # Step 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None  # No cycle

        # Step 2: Find starting node of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

# Creating a cycle list: 3 -> 2 -> 0 -> -4 -> back to 2
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # cycle here

obj = Solution()
cycle_node = obj.detectCycle(node1)
print(cycle_node.val)  # Output: 2
