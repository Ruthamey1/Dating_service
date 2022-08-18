class Dating:

    def __init__(self):
        pass
       

    def open_file(self):
        try:
            f = open('/Users/ruthamey/Documents/Basic_projects/user_info.txt')
            all_lines = f.readlines()
        except FileNotFoundError:
            print('File not found')
        return all_lines
