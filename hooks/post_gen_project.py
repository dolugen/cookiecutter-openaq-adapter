import os
import random
import shutil
import string

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

'''
Workaround for CC's project based generation
'''

def remove_cc_dir():
    print('Removing unused directory...')
    os.rmdir(PROJECT_DIRECTORY)

def move_adapter_file():
    print('Moving {{ cookiecutter.adapter_name }}.js to adapters directory...')
    adapter_path = os.path.join(PROJECT_DIRECTORY, '{{ cookiecutter.adapter_name }}.js')
    target_path = os.path.join(PROJECT_DIRECTORY, '../adapters', '{{ cookiecutter.adapter_name }}.js')
    os.rename(adapter_path, target_path)
    
move_adapter_file()
remove_cc_dir()
