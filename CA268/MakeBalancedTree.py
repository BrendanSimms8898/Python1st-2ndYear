def make_list(lst):
	end, endnt = [], []
	notend = sorted(lst)
	end.append(notend.pop(len(lst)//2))
	if len(notend)>0:
		endnt.append(notend[:len(lst)//2])
		endnt.append(notend[len(lst)//2:])
		while len(end) != len(lst):
			if endnt[0] != []:
				end.append(endnt[0][len(endnt[0])//2])
				a = endnt.pop(0)
				endnt.append(a[:len(a)//2])
				endnt.append(a[len(a)//2+1:])
			else:
				endnt.pop(0)
	return end

#a function which takes a list as an argument and rearranges the list 
#(or produces a new list with the same elements) so that when each item is added to the list, the tree will be perfectly balanced.
