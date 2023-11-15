'''
add string 0000 ,0001,0002...9999 to each line's last
example original:
    1333333
    1333334
    1333335
    1333336

example output:
    13333330000
    13333330001
    13333330002
    ...
    13333339999
    13333340000
'''
import os

def read_file_from_list(file_path):
    '''
        make a string list from txt file by apointed file path
    '''
    with open(file_path, 'r') as file:
        content = file.readlines()
        return [line.strip() for line in content]

def add_str_to_line(original_str,str_list):
    '''
    add every str of list to original_str last position and make a new line
    '''
    #var
    list_result=[]
    #program
    for line in str_list:
        list_result.append(original_str+line)
    return list_result

def get_filename_without_extension(file_path):
    base_name = os.path.abspath(file_path)
    return os.path.splitext(base_name)[0]
    

if __name__=="__main__":
    # var
    read_file_path=r"D:\\number.txt"
    save_file_path=get_filename_without_extension(read_file_path)+"_result.txt"
    save_list=[]

    #cmd lines
    print("Check python path is ok!")
    last_str_list = [str(num).zfill(4) for num in range(10000)]
    read_list=read_file_from_list(read_file_path)

    for read_line in read_list:
        tmp_list=add_str_to_line(read_line,last_str_list)
        save_list.extend(tmp_list)

    # save the string list to file
    with open(save_file_path, 'w') as file:
        for item in save_list:
            file.write(f"{item}\n")

    print("save to "+ save_file_path+"!")
