"""
Assignment1> Load the file with the values every. The file must be in the same directory with the name 
  >>> values.txt

"""
import math


class Node(object):
	
	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next

class LinkedList(object):

	def __init__(self):
		self.head = None

	def add(self, value):
		node = Node(value, self.head)
		self.head = node

	def remove(self, value):
		current = self.head
		previous = None
		# search the node with the data. 
		# Keep in memory the previous to validate when it is head so point the new head
		while current:
			if current.value == value:
				break
			else:
				previous = current
				current = current.next
		if current is None:
			raise ValueError('No se encontró el elemento')
		if previous is None:
			self.head = current.next
		else:
			previous.next = current.next

	def get_prior(self):
		return self.head

	# Get the node next to the node with match with the value
	def get_next_by_value(self, value):
		current = self.head
		while current:
			if current.value == value:
				return current.next
			else:
				current = current.next

		if current is None:
			raise ValueError('No se encontró el elemento')

	# Get the next node
	def __getitem__(self, index):
		nd = self.head
		for i in range(0,index):
			if nd.next is None:
				raise StopIteration
			nd = nd.next
		return nd

print('App initiated...')
print('Loading file value.txt')
f = open('values.txt', 'r+')
print('File values.txt loaded')
n = 0
sum_val = 0
line_val = None
mean = None
dev = None
list_vals = LinkedList()
print('Loading values in LinkedList')
for line in f:
	if str(line).rstrip('\r') != '':
		n+=1
		try:
			line_val = float(str(line))
			list_vals.add(line_val)
		except ValueError:
			print('Error al intentar convertir el valor '+line+'.')
			raise ValueError('Imposible convertir el valor '+line+'.')
print("--------------------------")
print('Calculating mean')
for nd in list_vals:
	sum_val += nd.value

mean = sum_val/n
#print('sum ='+str(sum_val))
print('MEAN = '+str(mean))
print('Calculating SD')
sum_val = 0
for nd in list_vals:
	x = (nd.value - mean) * (nd.value - mean)
	sum_val+=x
#print('Sumatoria (Xi-Xavg)^2 = '+str(sum_val))
dev = math.sqrt(sum_val/(n-1))
print('SD = '+str(dev))