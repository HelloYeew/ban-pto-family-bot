def read_ban_file():
    my_file = open("ban_link_list.txt", "r")
    content_list = my_file.readlines()
    ban_list = []
    for i in content_list:
        ban_list.append(i[:-1])
    return ban_list


def write_file(file_name, text):
    with open(file_name, 'a') as filehandle:
        filehandle.writelines(f"\n{text}")
