import os, sys
from sortedcontainers import SortedDict 

def dir_walk_sorted_all(path:str):
    """
    Prints sorted list of files under the directory (ASC order)

    SortedDict. Keeps our dict/hasmap sorted by key. 
    Values are list of tuples. List have length >1 if multiple files have the same size
       BYTES        PATH          NAME
     {
        123: ('/home/project/', 'file1')
        499: ('/home/project/', 'file3')
        523: [('/home/project/', 'file2'), ('/home/project/', 'file4')]  # same size
     }

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