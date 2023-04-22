import os, sys

os.chdir(sys.path[0])

os.system('python setup.py sdist bdist_wheel')

os.system('~/.local/bin/twine upload dist/*')