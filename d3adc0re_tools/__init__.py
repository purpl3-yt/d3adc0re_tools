__version__ = '0.0.1'
__creator__ = 'Purpl3'

print('''
  ____ _____           _       ___             _____           _     
 |  _ \___ /  __ _  __| | ___ / _ \ _ __ ___  |_   _|__   ___ | |___ 
 | | | ||_ \ / _` |/ _` |/ __| | | | '__/ _ \   | |/ _ \ / _ \| / __|
 | |_| |__) | (_| | (_| | (__| |_| | | |  __/   | | (_) | (_) | \__ \\
 |____/____/ \__,_|\__,_|\___|\___/|_|  \___|   |_|\___/ \___/|_|___/
                                                                     by purpl3''')

# Clean pycache folders
import pathlib, shutil; [shutil.rmtree(p.__str__()) for p in pathlib.Path('.').rglob('__pycache__')]

# Import programs
from . import PyProxy
from . import SongDownloader