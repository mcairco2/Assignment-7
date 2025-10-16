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




#-------------------- DESIGN MEMO --------------------

# A binary tree is the ideal structure for modeling the doctor hierarchy because it captures
# the parent–child relationships of supervisors and their direct reports. Each doctor node can
# have up to two subordinates, mirroring the structure of many real-world organizational
# charts. Trees provide a natural way to visualize and traverse hierarchical relationships,
# allowing efficient recursive operations like reporting, search, and updates.

# Traversal types represent different real-world workflows. Preorder traversal (root-left-right)
# is best when we want to process a supervisor before their team—for example, generating
# reports or sending top-down communications. Inorder traversal (left-root-right) is useful for
# ordered processing or reviews where both sides of a structure are balanced. Postorder
# (left-right-root) fits bottom-up workflows, like aggregating team performance or cleaning up
# data before deleting higher-level nodes.

# A min-heap is ideal for managing emergency intake because it always allows instant access to
# the highest-priority (lowest urgency value) patient in O(1) time while keeping insertions and
# removals efficient at O(log n). The heap ensures real-time reordering of patients as new cases
# arrive, simulating the triage system hospitals use in emergencies. This efficient structure
# supports fairness and responsiveness under constant load, key requirements in healthcare and
# other real-time systems.
