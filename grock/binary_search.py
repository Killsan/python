def binary_search(list, item):
	low = 0
	hight = len(list)-1
	while low <= hight:
		mid = (low + hight)
		gues = list[mid]
		if gues == item:
			return mid
		if gues > item:
			hight = mid -1 
		else:
			low = mid + 1
			return None
my_list = [1, 23, 43 , 54, 322, 2313]
my_list.sort()
print(binary_search(my_list, 2313))