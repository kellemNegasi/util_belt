


def list_to_txt(list_object,file_dest='./list.txt'):
    with open(file_dest, 'w') as f:
        for item in list_object:
            f.write("%s\n" % item)
        print(f'written a list of length {len(list_object)} to {file_dest}')

def list_from_txt(file_src):
    list_ = []
    # open file and read the content in a list
    with open(file_src, 'r') as filehandle:
        list_ = [current_place.rstrip() for current_place in filehandle.readlines()]
    return list_