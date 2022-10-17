
class Node:
	# конструктор
	def __init__(self, key):
		self.left = None
		self.right = None
		self.key = key
# будуємо дерево 
def insert(node, key): 
	if node is None:
		return Node(key)
	else:
		if node.key == key:
			return node
		elif node.key < key:
			node.right = insert(node.right, key)
		else:
			node.left = insert(node.left, key)
	return node
	# функція для пошуку в дереві
def search(root,key):
	
	if root is None or root.key == key:
		return root
											# Якщо значення присутнє в дереві то повертаємо його
											# якщо ж ні то повертаємо функцію
											
	if root.key < key:
		return search(root.right,key)

	return search(root.left,key)
	# функцція для побудови дерева користувачем
def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.key, end=" ")
		inorder(root.right)
def printTree(root, space=0, LEVEL_SPACE=5):
    if root == None:
        return
    space += LEVEL_SPACE
    printTree(root.right, space)
    for i in range(LEVEL_SPACE, space):
        print(end=" ")
    print("|" + str(root.key) + "|")
    printTree(root.left, space)

# Для переверірки на мінімальне значення в дереві
def minValueNode(node):
	current = node

	while(current.left is not None):
		current = current.left
	return current.key
# Для переверірки на максимальне значення в дереві
def maxValueNode(node):
	current = node

	while(current.right is not None):
		current=current.right
	return current.key

	# функція для знаходження наступного або попереднього по величині значення від заданого
def findPreSuc(root, key):
	if root is None:
		return
	if root.key == key:
		if root.left is not None:
			tmp = root.left
			while(tmp.right):
				tmp = tmp.right
			findPreSuc.pre = tmp


		if root.right is not None:
			tmp = root.right
			while(tmp.left):
				tmp = tmp.left
			findPreSuc.suc = tmp

		return
	if root.key > key :
		findPreSuc.suc = root
		findPreSuc(root.left, key)

	else: 
		findPreSuc.pre = root
		findPreSuc(root.right, key)

		# видалення дерева
def deleteNode(root, key):

	if root is None:
		return root

	if key < root.key:
		root.left = deleteNode(root.left, key)

	elif(key > root.key):
		root.right = deleteNode(root.right, key)

	else:

		if root.left is None:
			temp = root.right
			root = None
			return temp

		elif root.right is None:
			temp = root.left
			root = None
			return temp

		temp = minValueNode(root.right)


		root.key = temp.key

		root.right = deleteNode(root.right, temp.key)

	return root


root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)


	

	# Для взаєиодії з користувачем і виклику заданої функції
while(True):
	print("Choose your function: ")
	print("1 for insert, 2 for search, 3 for delete, 4 for successor, 5 for predecessor, 6 for min value, 7 for max value, 8 to show tree")
	a=int(input())
	if a==1:
		print("Choose value to input")
		b=int(input())
		root=insert(root, b)
		printTree(root)
	elif a==2:
		print("Choose value to input")
		c=int(input())
		root=search(root, c)
		if search(root, c)==None:
			print("Value is not in the tree")
		printTree(root)
	elif a==3:
		print("Choose value to delete")
		d=int(input())
		root=deleteNode(root, d)
		printTree(root)
	elif a==4:
		print("Choose start value")
		e=int(input())
		findPreSuc(root, e)
		if findPreSuc.suc is not None:
			print ("Successor is", findPreSuc.suc.key)
		else:
			print ("No Successor")
		printTree(root)
	elif a==5:
		print("Choose start value")
		g=int(input())
		findPreSuc(root, g)
		if findPreSuc.pre is not None:
			print ("Preccessor is", findPreSuc.pre.key)
		else:
			print("No preccessor")
		printTree(root)
	elif a==6:
		print("Min value in tree is:")
		print(minValueNode(root))
		printTree(root)
	elif a==7:
		print("Max value in tree is:")
		print(maxValueNode(root))
		printTree(root)
	elif a==8:
		printTree(root)

	




