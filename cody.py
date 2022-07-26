import sys
import os

# -f filename
FILE_NAME_TAG = '-f'
OUTPUT_FOLDER_NAME_TAG = '-o'
NEW_FILE_NAME_TAG = '-n'

DEFAULT_OUTPUT_FOLDER = 'output'

def getNewFileName():
  try:
    return sys.argv[sys.argv.index(NEW_FILE_NAME_TAG) + 1]
  except ValueError:
    print('No new file name was given, make sure to input -n <new file name>')

  return

def getOutputFolderName():
  try:
    return sys.argv[sys.argv.index(OUTPUT_FOLDER_NAME_TAG) + 1]
  except ValueError:
    print('No output folder name was given, make sure to input -o <output folder name>')

  return

def getFileName():
  try:
    return sys.argv[sys.argv.index(FILE_NAME_TAG) + 1]
  except ValueError:
    print('No filename was given, make sure to input -f <filename>')

  return

def args():
  if len(sys.argv) == 1:
    print("""

###############################################################
#                                                             #
#     -----------   -----------  -------       \        /     #
#     |             |         |  |       \      \      /      #
#     |             |         |  |        |      \    /       #
#     |             |         |  |        |       \  /        #
#     |             |         |  |        |        \/         #
#     |             |         |  |       /          |         #
#     -----------   -----------  -------            |         #
#                                                             #
###############################################################

Welcome to a coding language created by gccody.
This is to test how well I can code big projects using my own general knowledge.

This language will be for multipurpose use and will be compiled using python code.
Using the compiled python code it will then be converted into an exe script.

TODO:
  - create basic premade variables
  - be able to create variables and manipulate them
  - be able to create a function
  - be able to have arguments for function and return statements
  - create try catch blocks
  - create easy to understand syntax
  - create for loops
  - create advanced looping
  - string, boolean, int, float, long, double, array, tuple
  - for, in, and, or, as, while, true, false, if, return, pass, try, catch, finally, null, println, print
""")
    return
  FILENAME = getFileName()
  OUTPUT_FOLDER = getOutputFolderName()
  NEW_FILE_NAME = getNewFileName()
  if FILENAME == None:
    return

  return FILENAME, OUTPUT_FOLDER, NEW_FILE_NAME

def basicCompile(data: str):
  data.replace

def main():
  FILENAME, OUTPUT_FOLDER, NEW_FILE_NAME = args()
  if FILENAME == None: return
  DIR = os.getcwd()
  FILE = open(f'{DIR}\\{FILENAME}', 'r', encoding='utf-8')
  FILE_DATA = FILE.read()
  FILE.close()
  BASIC_COMPILED_DATA = basicCompile(FILE_DATA)
  with open(f'{DIR}\\{OUTPUT_FOLDER if OUTPUT_FOLDER else DEFAULT_OUTPUT_FOLDER}\\{NEW_FILE_NAME if NEW_FILE_NAME else FILENAME}.py', 'w', encoding='utf-8') as F:
    F.write(BASIC_COMPILED_DATA)

if __name__ == '__main__':
  main()