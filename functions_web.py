FILEPATH = 'todos.txt'
def open_file(filepath=FILEPATH):
    """
    Function used to open and return contents of todos.txt
    :param filepath: todos.txt used as default path
    :return: Function returns the contents of todos.txt file
    """
    with open(filepath, 'r') as file_read:
        read_data = file_read.readlines()
    return read_data


def write_file(write_item, filepath=FILEPATH):
    """ Write the to-do items into the text file"""
    with open(filepath, 'w') as file_write:
        file_write.writelines(write_item)


if __name__ == '__main__':
    print(open_file())
