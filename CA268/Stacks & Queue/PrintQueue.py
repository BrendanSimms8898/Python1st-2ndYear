def print_queue(lst, front, back):
	if back < front:
		for item in lst[front:]:
			print(item)
		for item in lst[:back]:
			print(item)
	else:
		for item in lst[front:back]:
			print(item)

#A Function which will take some queue parameters and return a list of the elements of the queue
