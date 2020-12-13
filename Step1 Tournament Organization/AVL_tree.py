class Node(object):
    def __init__(self, player):
        self.left = None
        self.right = None
        self.player = player
        self.height=1

class AVL_Tree(object): 

	# Recursive function to insert key in subtree rooted with node and returns new root of subtree. 
    def insert(self, root, player): 
	
		# Step 1 - Perform normal BST 
        if not root: 
            return Node(player) 
        elif player.score < root.player.score: 
            root.left = self.insert(root.left, player) 
        else: 
            root.right = self.insert(root.right, player) 

		# Step 2 - Update the height of the ancestor node 
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right)) 

		# Step 3 - Get the balance factor 
        balance = self.getBalance(root) 

		# Step 4 - If the node is unbalanced, then try out the 4 cases 
		# Case 1 - Left Left 
        if balance > 1 and player.score < root.left.player.score: 
            return self.rightRotate(root) 

		# Case 2 - Right Right 
        if balance < -1 and player.score >= root.right.player.score: 
            return self.leftRotate(root) 

		# Case 3 - Left Right 
        if balance > 1 and player.score >= root.left.player.score: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 

		# Case 4 - Right Left 
        if balance < -1 and player.score < root.right.player.score: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
        return root 
    
    def delete(self, root, player): 
  
        # Step 1 - Perform standard BST delete 
        if not root: 
            return root 
        elif player.score < root.val: 
            root.left = self.delete(root.left, player) 
        elif player.score > root.val: 
            root.right = self.delete(root.right, player) 
        else: 
            if root.left is None: 
                temp = root.right 
                root = None
                return temp 
            elif root.right is None: 
                temp = root.left 
                root = None
                return temp 
            temp = self.getMinValueNode(root.right) 
            root.val = temp.val 
            root.right = self.delete(root.right,temp.val) 
  
        # If the tree has only one node, 
        # simply return it 
        if root is None: 
            return root 
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and self.getBalance(root.left) >= 0: 
            return self.rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and self.getBalance(root.right) <= 0: 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and self.getBalance(root.left) < 0: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and self.getBalance(root.right) > 0: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 


    def leftRotate(self, z): 

        y = z.right 
        T2= y.left 

		# Perform rotation 
        y.left = z 
        z.right = T2 

		# Update heights 
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right)) 

		# Return the new root 
        return y 

    def rightRotate(self, z): 

        y = z.left 
        T3 = y.right 

		# Perform rotation 
        y.right = z 
        z.left = T3 

		# Update heights 
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right)) 

		# Return the new root 
        return y 

    def getHeight(self, root): 
        if not root: 
            return 0
        return root.height 

    def getBalance(self, root): 
        if not root: 
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right) 

    
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.player)
            res = res + self.inorderTraversal(root.right)
        return res
    
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.player)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res
    
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.player)
        return res

def CreateAVL(list_players):
    AVL = AVL_Tree()
    root=None
    for player in list_players:
        root=AVL.insert(root,player)
    return AVL, root
