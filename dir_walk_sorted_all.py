import os, sys
from sortedcontainers import SortedDict 

def dir_walk_sorted_all(path:str):
    """
    Prints sorted (ASC) list of all files under the directory including the sub directories
    
    SortedDict. Keeps our dict/hasmap sorted by key. 
    Values are list of tuples. List have length >1 if multiple files have the same size
       BYTES        PATH          NAME
     {
        123: ('/home/project/', 'file1')
        499: ('/home/project/', 'file3')
        523: [('/home/project/', 'file2'), ('/home/project/', 'file4')]  # same size
     }

     Example:
        /home/bearwebua/projects/a/api || .dockerignore || 22 B
        /home/bearwebua/projects/a/api || requirements.txt || 60 B
        /home/bearwebua/projects/a/api/src || logger.py || 285 B
        /home/bearwebua/projects/a/api || Dockerfile - Copy || 341 B
        /home/bearwebua/projects/a/api || Dockerfile || 341 B
        /home/bearwebua/projects/a/api/src/__pycache__ || logger.cpython-38.pyc || 399 B
        /home/bearwebua/projects/a/api/config || production.py || 710 B
        /home/bearwebua/projects/a/api/config || development.py || 716 B
        /home/bearwebua/projects/a/api/src || utils.py || 1891 B
        /home/bearwebua/projects/a/api/src || exceptions.py || 1923 B
        /home/bearwebua/projects/a/api/src/__pycache__ || utils.cpython-38.pyc || 2029 B
        /home/bearwebua/projects/a/api || .gitignore || 2034 B
        /home/bearwebua/projects/a/api/src/__pycache__ || exceptions.cpython-38.pyc || 2151 B
        /home/bearwebua/projects/a/api/tests || test_one.py || 2197 B
        /home/bearwebua/projects/a/api/src || response.py || 2680 B
        /home/bearwebua/projects/a/api/src/__pycache__ || response.cpython-38.pyc || 3340 B
        /home/bearwebua/projects/a/api || index.py || 5375 B
        /home/bearwebua/projects/a/api/__pycache__ || index.cpython-38.pyc || 5407 B
        /home/bearwebua/projects/a/api/config || db_production.db || 8192 B
    """

    sorted_dict = SortedDict({})

    for root, dirs, files in os.walk(path): # recurisve O(n) to traverse all the nodes
        for file in files: 
            size = os.stat(os.path.join(root, file)).st_size
            # insertion to SortedDict: O(log n)
            if size in sorted_dict:
                if type(sorted_dict[size]) is list:
                    sorted_dict[size].append((root, file)) # increase the list size since another file have the same size
            else:
                sorted_dict[size] = [(root, file)]

    # data structure is ready and sorted. Let's print it
    for key, val in sorted_dict.items():
            for item in val:
                print ("{} || {} || {} B".format(item[0], item[1], key))

           
dir_walk_sorted_all(sys.argv[1])       
# example: `$ python3 dir_walk_sorted.py "/home/username/projects/myproject/api"`