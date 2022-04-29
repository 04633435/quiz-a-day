from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution():
    def merge_nodes(self, head):
        cur = head
        node_number = []
        start = False
        end = True
        sum = 0
        while cur:
            if cur.val == 0 and start == False and end == True:
                start = True
                end = False
                cur = cur.next
                continue
            elif cur.val != 0 and start and not end:
                sum += cur.val
                cur = cur.next
            elif cur.val == 0 and start and not end:
                node_number.append(sum)
                sum = 0
                cur = cur.next
        print(node_number)
        ret = ListNode(node_number[0])
        cur = ret
        for i in range(1, len(node_number)):
            node = ListNode(node_number[i])
            cur.next = node
            cur = node
        return ret


if __name__ == "__main__":
    s = Solution()
    n = [0,3,1,0,4,5,2,0]
    head = ListNode()
    cur = head
    for i in range(1, len(n)):
        node = ListNode(n[i])
        cur.next = node
        cur = node
    print(s.merge_nodes(head))