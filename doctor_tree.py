class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None



class DoctorTree:
    def __init__(self):
        self.root = None

    def _find_node(self, node, name):
        if node is None: 
            return None
        if node.name == name:
            return node 
        
        left_result = self._find_node(node.left, name)
        if left_result:
            return left_result
        return self._find_node(node.right, name)
    
    def insert(self, parent_name, child_name, side):
        if side not in ("left", "right"):
            raise ValueError("Side must be 'left' or 'right'")
        
        if self.root is None:
            self.root = DoctorNode(child_name)
            return
        
        parent_node = self._find_node(self.root, parent_name)
        if not parent_node:
            raise ValueError(f"Parent '{parent_name}' not found in the tree.")
        
        new_node = DoctorNode(child_name)

        if side == "left":
            if parent_node.left: 
                raise ValueError(f"{parent_name} already has a left report.")
            parent_node.left = new_node
        else:
            if parent_node.right:
                raise ValueError(f"{parent_name} already has a right report.")
            parent_node.right = new_node
# ------------------ Traversals ------------------

    def preorder(self, node):
        """Root → Left → Right"""
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        """Left → Root → Right"""
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        """Left → Right → Root"""
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


# ------------------ TEST SECTION ------------------
if __name__ == "__main__":
    # Create the tree and insert doctors
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")
    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    # Print traversals
    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))





