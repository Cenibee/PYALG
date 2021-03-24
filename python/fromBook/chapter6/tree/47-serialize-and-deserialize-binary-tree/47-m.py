# Definition for a binary tree node.
from typing import Deque, List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def partial_serialize(node: TreeNode) -> List[str]:
            if not node:
                return ['n']
            elif not node.left and not node.right:
                return [str(node.val)]
            else:
                return [str(node.val), ':',\
                    *partial_serialize(node.left), '|',\
                    *partial_serialize(node.right)]
        return ''.join(partial_serialize(root))

    pos = 0
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # val을 가리키면서 시작하고, val을 가리키면서 끝난다.
        def partial_deserialize() -> TreeNode:
            if self.pos >= len(data):
                return None

            if data[self.pos] == 'n':
                self.pos += 1
                node = None

            else:
                start = self.pos
                while len(data) > self.pos and\
                    (data[self.pos] != ':' and data[self.pos] != '|'):
                        self.pos += 1
                node = TreeNode(int(data[start:self.pos]))

            self.pos += 1
            if self.pos < len(data) and data[self.pos - 1] == ':':
                self.pos += 1
                node.left = partial_deserialize()
                node.right = partial_deserialize()
            return node
        result = partial_deserialize()
        self.pos = 0
        return result




# Your Codec object will be instantiated and called as such:
# ser = Codec()
def fulfil_tree(l: List[int]) -> TreeNode:
    root = TreeNode(l[0])
    q = Deque([root])
    i = 1

    while q and i < len(l):
        node = q.popleft()
        if l[i]:
            node.left = TreeNode(l[i])
            q.append(node.left)
        i += 1

        if i >= len(l):
            break
        if l[i]:
            node.right = TreeNode(l[i])
            q.append(node.right)
        i += 1
    return root


# deser = Codec()
# print(deser.serialize(fulfil_tree([1,2,3,None,None,4,5])))
# ans = deser.deserialize('10:22|33:44:66|n|51')

deser = Codec()
tree = fulfil_tree([1,2,3,None,None,4,5,6,7])
test = deser.serialize(tree)
a = deser.deserialize(test)
print('test')