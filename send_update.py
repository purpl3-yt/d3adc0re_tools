# This script for developer to upload new versions

import os, sys, shutil

os.chdir(sys.path[0])

os.system('python setup.py sdist bdist_wheel')

os.system('~/.local/bin/twine upload dist/*')

for f in ['dist', 'build', 'D3adC0re_Tools.egg-info', '__pycache__']:
    shutil.rmtree(f)