# for loop solution

class Node():
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next
	def get_content(self):
		return self.data

class Linkedlist():
	def __init__(self):
		self.first_node = None
		self.last_node = None
	def add_node(self,data):
		new_node = Node(data = data)
		if self.first_node == None:
			self.first_node = new_node
			self.last_node = new_node

def del_node(self, data=None):
	pass

def gen_sorted_list(my_dict):
	my_list = []
	for key, value in my_dict.iteritems():
		if value == 1:
			my_list.append(key)
	my_list.sort()
	return my_list

def main():

	my_dict = {}

	for i in range (1,101):
		my_dict[i] = 1

	my_list = gen_sorted_list(my_dict)

	remove_first = False 	# initialize - first round, keep #1,3,5...
	length = len(my_list)

	while length > 1:
		if remove_first:	
			for index in range(length):
				if (index+1)%2 == 0:
					my_dict[my_list[index]] = 0
		else:
			for index in range(length):
				if index%2 == 0:
					my_dict[my_list[index]] = 0

		if my_dict[my_list[length-1]] == 0: 
			remove_first = True
		else:
			remove_first = False

		my_list = gen_sorted_list(my_dict)

		length = len(my_list)
		print my_list, length

if __name__ == "__main__":
	main()