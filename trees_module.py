# TREE CLASS
# Each clothing categoriy will be structured as a tree.
# E.g Bags (root node) -> backpacks, bum bags, sling bags (children node) -> Designer, colour, price (leaf nodes)

from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        # print("Initializing a clothing node...")
    
    def add_child(self, *nodes):
        for child_node in nodes:
            self.child_node = child_node
            self.children.append(child_node)
            # print(f"Adding {child_node.value} to {self.value}...")

    def remove_child(self, child_node):
        self.children = [child for child in self.children if child is not child_node]
        # print(f"Removing {child_node.value} from {self.value}...")

    def __str__(self):
        stack = deque()
        stack.append([self, 0])
        str_level = "\n"
        while len(stack) > 0:
            node, level = stack.pop()
            if level > 0:
                str_level += "| "*(level - 1)+ "|-"
            str_level += str(node.value)
            str_level += "\n"
            level += 1
            for child_node in reversed(node.children):
                stack.append([child_node, level])
        return str_level
    
