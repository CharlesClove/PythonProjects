import os
def scan_for_files_bigger_than_given(max_size):
    path = '/home/kg/Pobrane'
    file_bucket = os.listdir(path)

    for file in file_bucket:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)/1024
            if file_size > max_size:
                print(f"File {file} is bigger than {max_size} MB")

if __name__ == '__main__':
    size_to_limit = input("State limit to narrow the output of search: ")
    try:
        size_to_limit = float(size_to_limit)
        scan_for_files_bigger_than_given(size_to_limit)
    except ValueError:
        print('Please enter a numeric value')


