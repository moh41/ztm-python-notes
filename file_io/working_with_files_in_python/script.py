my_file = open('test.txt')

print(my_file.read())
my_file.seek(0) # move the cursor to the beginning of the file
print('---')
print(my_file.readline())
print(my_file.readlines())

my_file.close()