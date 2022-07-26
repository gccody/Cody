import sys
import os

# -f filename
FILE_NAME_TAG = '-f'

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
  if FILENAME == None:
    return

  return FILENAME

def main():
  FILENAME = args()
  if FILENAME == None: return
  DIR = os.getcwd()
  FILE = open(f'{DIR}\\{FILENAME}', 'r', encoding='utf-8')
  print(FILE.read())

if __name__ == '__main__':
  main()