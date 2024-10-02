#Create a code that writes name & genus of your animals to a text file.
my_file = "animals.txt"
file = open(my_file, 'w')
for i in my_animals:
    file.write(i.name)
    file.write(" ")
    file.write(f"{i.genus} \n")
file = open(my_file, 'r')
text = file.read()
file.close()
print(text)