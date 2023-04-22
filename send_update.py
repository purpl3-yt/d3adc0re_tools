import os, sys

os.chdir(sys.path[0])

os.system('~/.local/bin/twine upload dist/*')