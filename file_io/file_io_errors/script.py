try:
    with open('potato.txt', 'r') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('File not found!')
    raise err
except IOError as err:
    print('IO error!')
    raise err