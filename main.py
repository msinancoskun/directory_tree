import os


path = os.getcwd()


class DirectoryTree:

    def __init__(self, main_directory):
        self.main_directory = main_directory
        self.tree = {}
        self.dir = []
        self.folder = {}
        self.files = []
        self.main_folder = ""
        self.files_to_ignore = ['venv', '.idea']

    def create_tree(self):
        for directory, folder, files in os.walk(self.main_directory):
            dir_name = directory.split('\\')[-1]
            folder_ = folder if len(folder) > 0 else []
            self.tree[dir_name] = folder_
            if dir_name in self.tree:
                for file in files:
                    self.tree[dir_name].append(file)
            else:
                for file in files:
                    self.tree[dir_name] = file

    def display_tree(self):
        final_list = []
        for key, value in self.tree.items():
            print('-', key)
            for val in value:
                print('\t--', val)


directory_generater = DirectoryTree(path)
directory_generater.create_tree()
directory_generater.display_tree()
