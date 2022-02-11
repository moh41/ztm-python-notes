# Reading
with open('test.txt', mode='r') as my_file:
    print(my_file.readlines())

# Reading and writing, cursor put to 0
with open('test.txt', mode='r+') as my_file:
    text = my_file.write('hey it\'s me!')
    print(text) # Prints how many characters were written
    print(my_file.readlines())

# Write (assume/create new file and delete contents within it)
with open('test.txt', mode='w') as my_file:
    text = my_file.write('hey it\'s me!')
    print(text) # Prints how many characters were written

# Appending
with open('test.txt', mode='a') as my_file:
    text = my_file.write('woah this is appended!')