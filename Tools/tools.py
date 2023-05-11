#!/usr/bin/python3
import argparse
import os

__version__ = 0.1

parser = argparse.ArgumentParser(
    prog='HackerRank Solutions CLI Tools',
    description='Tools to create directories and file structures quickly.'
)

parser.add_argument('--dir', help='Root Directory', required=False)
parser.add_argument('--files', help='List of file names to construct', required=False)
parser.add_argument('name', help='Name to use for assets.')

class main:

    def __init__(self, args):
        self.name = args.name
        self.root_dir = os.path.abspath(args.dir) if args.dir else os.getcwd()
        self.files_to_create = [f'{self.name}.py', f'{self.name}.ipynb', 'README.md']
        self.new_path = None
    def create_dir(self, name, root):
        self.new_path = os.path.join(root, name)
        try:
            os.mkdir(self.new_path)
        except OSError as err:
            print(f'Unable to create directory: {err}')
            print('Now exiting')
            exit()

        else:
            print(f'Successfully created new directory: {self.new_path}')
    
    def create_files(self, names, root = None):
        root = root if root else self.new_path
        success = ['Successfully Created:']
        failures = ['Failed to Create: ']
        for i in names:
            try:
                with open(os.path.join(root, i), 'a') as fp:
                    pass
                success.append(i)
            except OSError as err:
                failures.append(i)
        if len(success) > 1: print(' '.join(success))
        if len(failures) > 1: print(' '.join(failures))

    def build(self):
        self.create_dir(self.name, self.root_dir)
        self.create_files(self.files_to_create)


if __name__ == "__main__":
    constructer = main(parser.parse_args())
    constructer.build()