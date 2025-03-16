class TreeNode:
    def __init__(self, value: int | str):
        self.value = value
        self.right = None
        self.left = None
    
class ExpressionTree:
    def __init__(self, postfix_expr: str) -> None:
        self.root = self.construct_expression_tree(postfix_expr)

    def construct_expression_tree(self, postfix: str) -> TreeNode:
        if not postfix:
            return None

        stack = []
        characters = postfix.split()
        
        for character in characters:
            if character.isdigit():
                node = TreeNode(int(character))
                stack.append(node)
            else:
                if len(stack) >= 2:
                    right = stack.pop()
                    left = stack.pop()
                node = TreeNode(character)
                node.right = right
                node.left = left
                stack.append(node)
        if stack:
            return stack.pop()
        else:
            return None
        
    def evaluate_expression(self) -> int | float:
        if not self.root:
            return 0
        
        def evaluation_recursive(node: TreeNode) -> int | float:
            if node is None:
                return 0
            
            if isinstance(node.value, int):  
                return node.value

            right_value = evaluation_recursive(node.right)
            left_value = evaluation_recursive(node.left)

            if node.value == '+':
                return left_value + right_value
            elif node.value == '-':
                return left_value - right_value
            elif node.value == '*':
                return left_value * right_value
            elif node.value == '/':
                if right_value == 0:
                    return float('inf')
                else:
                    return left_value / right_value
            
        return evaluation_recursive(self.root)
    
    def get_inorder_expression(self) -> str:
        if self.root is None:
            return ""
        
        def inorder_recursive(node: TreeNode) -> str:
            if not node:
                return ""
            
            if isinstance(node.value, int):  
                return node.value
            
            right_value = inorder_recursive(node.right)
            left_value = inorder_recursive(node.left)

            return f'({left_value}{node.value}{right_value})'
        
        return inorder_recursive(self.root)