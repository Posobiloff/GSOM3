# 2. This code counts the number of str elements within the list
my_list = [1, 'jentacular', ['white', 'black', 'green', 'yellow'],
           'javelin', 'jeopardy', 73, 189, ['He', 'is', 'an', 'Englishman'], 'Jeronimo', 'Joker']
count_str = 0
for i in my_list:
    if type(i) == str:
        count_str +=1
print ("The number of string elements in the list", count_str)