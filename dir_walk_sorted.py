import os, sys

def dir_walk_sorted(path:str)->None:

    if not type(path) is str or not path:
        return ''
    
    for root, dirs, files in os.walk(path): # recurisve
        # sort only in sub dirs
        files = sorted(files, key = lambda x: os.stat(os.path.join(root, x)).st_size) # O(n*log(n))
        for file in files: # O(n)
            print ("{} || {} || {} B".format(root, file, os.stat(os.path.join(root, file)).st_size))

dir_walk_sorted(sys.argv[1])       
# example: `$ python3 dir_walk_sorted.py "/home/username/projects/myproject/api"`