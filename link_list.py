# Iterative Python program to search 
# an element in linked list
import random,time,string
word_num = {}
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alphabet = [i for i in alphabet]
# Node class
class Node:
	
	# Function to initialise the 
	# node object
	def __init__(self, data):
	
		# Assign data
		self.data = data 

		# Initialize next as null
		self.next = None

# Linked List class
class LinkedList:
	def __init__(self):

		# Initialize head as None
		self.head = None

	# This function insert a new node at the
	# beginning of the linked list
	def push(self, new_data):
	
		# Create a new Node
		new_node = Node(new_data)

		# 3. Make next of new Node as head
		new_node.next = self.head

		# 4. Move the head to point to new Node
		self.head = new_node

	# This Function checks whether the value
	# x present in the linked list 
	# def search(self, x):

	# 	# Initialize current to head
	# 	current = self.head

	# 	# Loop till current not equal to None
	# 	while current != None:
	# 		if current.data == x:

	# 			# Data found
	# 			return True
			
	# 		current = current.next
		
	# 	# Data Not found
	# 	return False
	def search(self, search_for):
		current = self.head
		count = 0

		# Loop till current not equal to None
		while current is not None:
			if current.data == search_for:
				count += 1
			current = current.next

		# Return the count
		return count


# Driver code
with open('FINarticle.txt',encoding="utf-8" ) as space:
    llist = LinkedList()
    Billy = space.read().lower()
    Billy = Billy.replace('ё','е')
    Billy_clean = ''
    for i in Billy:
        if i not in alphabet:
            Billy_clean += ' '
        else:
            Billy_clean += i
    Billy_clean = Billy_clean.split()
    Billy_clean = [string for string in Billy_clean if len(string) >= 4]

    Billy_clean = sorted(Billy_clean)
    bilset = list(set(Billy_clean))
    
    
    print(bilset,'\n')
    for i in bilset:
        word_num[i] = len(word_num)
    print(word_num, '\n')
    word_freq = word_num
    keys = []
    for i in Billy_clean:
        keys.append(word_num[i])
    keys = sorted(keys)
    for i in keys:
        llist.push(i)
    for j in bilset:
        val = word_num[j]
        word_freq[j] = llist.search(val)
        print(j, word_freq[j])

        
        
sorted_freq = dict(sorted(word_freq.items(), key=lambda item: item[1])) 
print(sorted_freq)
# Start with the empty list


# # Use push() to construct list
# # 14->21->11->30->10 
# llist.push(10)
# llist.push(21)
# llist.push(30)
# llist.push(11)
# llist.push(21)
# llist.push(14)

# # occurrences = llist.search(21)
# print(f"21 occurs {occurrences}")
# # This code is contributed by Ravi Shankar
