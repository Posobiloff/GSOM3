import find_two_smallest as fts
import Integers_difiner as Id
my_file = "The results"
file = open(my_file, 'w')
for i in Id.lists_int:
     small = fts.find_two_samllest(i)
     file.write(f"The two smallest numbers in {i} are {small} \n")
file.close()