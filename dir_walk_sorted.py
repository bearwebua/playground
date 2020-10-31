import os, sys

def dir_walk_sorted(path:str)->None:
    """
    Prints sorted (ASC) list of all files under the same directory

    Example:
        /home/bearwebua/projects/a/api || .dockerignore || 22 B
        /home/bearwebua/projects/a/api || requirements.txt || 60 B
        /home/bearwebua/projects/a/api || Dockerfile - Copy || 341 B
        /home/bearwebua/projects/a/api || Dockerfile || 341 B
        /home/bearwebua/projects/a/api || .gitignore || 2034 B
        /home/bearwebua/projects/a/api || index.py || 5375 B
        /home/bearwebua/projects/a/api/src || logger.py || 285 B
        /home/bearwebua/projects/a/api/src || utils.py || 1891 B
        /home/bearwebua/projects/a/api/src || exceptions.py || 1923 B
        /home/bearwebua/projects/a/api/src || response.py || 2680 B
        /home/bearwebua/projects/a/api/src/__pycache__ || logger.cpython-38.pyc || 399 B
        /home/bearwebua/projects/a/api/src/__pycache__ || utils.cpython-38.pyc || 2029 B
        /home/bearwebua/projects/a/api/src/__pycache__ || exceptions.cpython-38.pyc || 2151 B
        /home/bearwebua/projects/a/api/src/__pycache__ || response.cpython-38.pyc || 3340 B
        /home/bearwebua/projects/a/api/__pycache__ || index.cpython-38.pyc || 5407 B
        /home/bearwebua/projects/a/api/tests || test_one.py || 2197 B
        /home/bearwebua/projects/a/api/config || production.py || 710 B
        /home/bearwebua/projects/a/api/config || development.py || 716 B
        /home/bearwebua/projects/a/api/config || db_production.db || 8192 B
    """

    if not type(path) is str or not path:
        return ''
    
    for root, dirs, files in os.walk(path): # recurisve. O(n)
        # sort only in sub dirs
        files = sorted(files, key = lambda x: os.stat(os.path.join(root, x)).st_size) # O(n*log(n))
        for file in files: # O(n)
            print ("{} || {} || {} B".format(root, file, os.stat(os.path.join(root, file)).st_size))

dir_walk_sorted(sys.argv[1])       
# example: `$ python3 dir_walk_sorted.py "/home/username/projects/myproject/api"`