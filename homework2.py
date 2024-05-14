def squared_list(num):
    squares = [i**2 for i in range(1, num + 1)]
    print(squares)

squared_list(5)

'''
This function has linear time complexity. It is iterating through the list and performing a constant-time (i**2) opperation on each item in the list.
'''

def reverse_slice(lst, i, j):
    lst[i:j+1] = reversed(lst[i:j+1])
    print(lst)

reverse_slice([1, 2, 3, 4, 5, 6, 7], 2,5)

'''
Time complexity of the above function depends on the size of the slice and reverse we have to do. Space complexity is constant because we have 
a finite 'n' in the origional list. No new lists or new indexes are being added or taken away. 
'''

def sorted_merged(lst1, lst2):
    lst3 = lst1 + lst2
    lst3.sort()
    print(lst3)

sorted_merged([1, 2, 6, 5, 4, 3, 7],[9,10,11,17,19])
sorted_merged(["ayden","jennifer","chris"],["clive","karen"])

'''
Time complexity of the above function depends solely on the sorting function O(N log n). Space complexity will depend on the size of our lists, 
the temporary space created to sort the list. 
'''