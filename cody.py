import re
import sys
import os
from unittest.mock import DEFAULT

# Console Tags
FILE_NAME_TAG = '-f'
OUTPUT_FOLDER_NAME_TAG = '-o'
NEW_FILE_NAME_TAG = '-n'
TAGS_LIST = [FILE_NAME_TAG, OUTPUT_FOLDER_NAME_TAG, NEW_FILE_NAME_TAG]

# Default folder output
DEFAULT_OUTPUT_FOLDER = 'output'

# Printing Tokens
PRINT_TOKEN = 'print'
PRINT_LINE_TOKEN = 'println'

# Regex
FUNCTION_REGEX = r'(def )[a-zA-Z0-9_]+(\((.*?)\))'
FUNCTION_REGEX_ERROR = r'(def )[a-zA-Z0-9_]+(\((.*?)\): )'
PRINT_REGEX = f'(prin[tln]+)(\()[\'"](.*?)[\'"](\))'
TRUTHY_REGEX = r'(.*?(?=\?))\?(.*?(?=:))\:(.*)'
TRUTH_REGEX_ERROR = r'(.*?(?=(if)))(.*?(?=(else)))(.*)'
MAIN_FUNCTION_REGEX = r'(def main())'

def getNewFileName() -> str | None:
  try:
    arg = sys.argv[sys.argv.index(NEW_FILE_NAME_TAG) + 1]
    if arg in TAGS_LIST:
      raise Exception('No file name was given, make sure to input -n <filename>')
    else:
      return arg
  except ValueError:
    return 
  except IndexError:
    raise Exception('No file name was given, make sure to input -n <filename>')

def getOutputFolderName() -> str | None:
  try:
    arg =  sys.argv[sys.argv.index(OUTPUT_FOLDER_NAME_TAG) + 1]
    if arg in TAGS_LIST:
      raise Exception('No output folder name was given, make sure to input -o <output folder name>')
    else:
      return arg
  except ValueError:
    return 
  except IndexError:
    raise Exception('No output folder name was given, make sure to input -o <output folder name>')

def getFileName() -> str | None:
  try:
    return sys.argv[sys.argv.index(FILE_NAME_TAG) + 1]
  except ValueError:
    print('No filename was given, make sure to input -f <filename>')

  return 

def args() -> list[str]:
  # Returns about the language
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
    return [None, None, None]

  FILENAME: str | None = getFileName()
  OUTPUT_FOLDER: str | None = getOutputFolderName()
  NEW_FILE_NAME: str | None = getNewFileName()

  return FILENAME, OUTPUT_FOLDER, NEW_FILE_NAME

def errorHandler(data):
  # Check if any functions are written incorrectly
  if re.search(FUNCTION_REGEX_ERROR, data):
    raise Exception('Function not create correctly, Nothing is needed to end the function initalization')
  if re.search(TRUTH_REGEX_ERROR, data):
    raise Exception('Truthy statement not create correctly, Ex: <bool> ? <true> : <false>')
  if not re.search(MAIN_FUNCTION_REGEX, data):
    raise Exception('Main function not created, make sure to create a main function')

def basicCompile(data: str):
  # Raise any errors
  errorHandler(data)

  # Format functions
  FUNCTION_MATCHES = re.finditer(FUNCTION_REGEX, data, re.MULTILINE)
  for MATCHNUM, MATCH in enumerate(FUNCTION_MATCHES, start=1):
    data = data.replace(MATCH.group(), f'{MATCH.group()}:')

  # Format print statements
  PRINT_MATCHES = re.finditer(PRINT_REGEX, data, re.MULTILINE)
  for MATCHNUM, MATCH in enumerate(PRINT_MATCHES, start=1):
    if MATCH.group().find('println') != -1:
      data = data.replace(MATCH.group(), f'print("{MATCH.group(3)}", end="\\n")')
    else:
      data = data.replace(MATCH.group(), f'print("{MATCH.group(3)}", end="")')

  # Format truthy statements
  data = data.replace('true', 'True')
  data = data.replace('false', 'False')
  TRUTHY_MATCHES = re.finditer(TRUTHY_REGEX, data, re.MULTILINE)
  for MATCHNUM, MATCH in enumerate(TRUTHY_MATCHES, start=1):
    data = data.replace(MATCH.group(), f'{MATCH.group(2).strip()} if {MATCH.group(1).strip()} else {MATCH.group(3).strip()}')


  data += """\n
if __name__ == '__main__':
  main()
  """

  return data

def main():
  FILENAME, OUTPUT_FOLDER, NEW_FILE_NAME = args()
  if FILENAME is None: return
  TRIMMED_DEFAULT_FILE_NAME = FILENAME.replace('.cy', '')
  DIR = os.getcwd()
  FILE = open(f'{DIR}\\{FILENAME}', 'r', encoding='utf-8')
  FILE_DATA = FILE.read()
  FILE.close()
  BASIC_COMPILED_DATA = basicCompile(FILE_DATA)
  FINAL_OUTPUT_FOLDER = OUTPUT_FOLDER if OUTPUT_FOLDER else DEFAULT_OUTPUT_FOLDER
  FINAL_FILE_NAME = NEW_FILE_NAME if NEW_FILE_NAME else TRIMMED_DEFAULT_FILE_NAME
  if not os.path.exists(f'{DIR}\\{FINAL_OUTPUT_FOLDER}'):
    os.mkdir(f'{DIR}\\{FINAL_OUTPUT_FOLDER}')
  with open(f'{DIR}\\{FINAL_OUTPUT_FOLDER}\\{FINAL_FILE_NAME}.py', 'w', encoding='utf-8') as F:
    F.write(BASIC_COMPILED_DATA)

if __name__ == '__main__':
  main()