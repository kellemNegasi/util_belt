


def list_to_txt(list_object,file_dest='./list.txt'):
    with open('your_file.txt', 'w') as f:
        for item in list_object:
            f.write("%s\n" % item)
        print(f'written a list of length{len(list_object)} to at {file_dest}')

def list_from_txt(file_src):
    places = []
    # open file and read the content in a list
    with open('listfile.txt', 'r') as filehandle:
        places = [current_place.rstrip() for current_place in filehandle.readlines()]