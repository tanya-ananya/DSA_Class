class TreeNode:
    def __init__(self, value: int | str):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self, postfix_expr: str) -> None:
        self.root = self.construct_expression_tree(postfix_expr)
        
    def construct_expression_tree(self, postfix: str) -> TreeNode:
        if not postfix:
            return None
        
        tree_stack = []
        characters = postfix.split()

        for character in characters:
            if character.isnum():
                tree_stack.append(TreeNode(int(character)))
            else:
                if tree_stack:
                    right = tree_stack.pop()
                    left = tree_stack.pop()
                new_node = TreeNode(character)
                new_node.left = left
                new_node.right = right
                tree_stack.append(new_node)
        if tree_stack:
            return tree_stack[-1]