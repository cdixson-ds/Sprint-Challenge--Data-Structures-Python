import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


from binary_search_tree import BSTNode

bst_1 = BSTNode(' ')
# bst_2 = BSTNode('Trevor Keith')

for i in names_1:
    #print(i)
    bst_1.insert(i)

print(bst_1.contains('Regina Molina'))

# for j in names_2:
#     bst_2.insert(j)

# duplicates = [j for j in names_2 if bst_2.contains(j)]

for i in names_2:
    if bst_1.contains(i):
        duplicates.append(i)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# runtime was 0.57 with bst, compared with approx. 20 seconds for the original 
# for loop. 

# the nexted loop has a runtime of O(n²)
# the bst has a runtime of O(log n)



# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
