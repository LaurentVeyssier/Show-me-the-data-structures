# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 11:11:33 2020

@author: lveys
"""
import os

# Search function with recursive approach
# Because no real order to the elements, the complexity of the search is O(n)
# we must go through each element with n the number of items to explore
def collect_files(path, filenames):
    """ Explore folder structure and collect all files 
    inputs: 
        path(str): path to search
        filenames(list): log of all filenames found in the structure
        
    Returns:
        a list of all the files found in the structure identified by their filepath
        """
    
    # collect all items in the folder
    filepaths = os.listdir(path)
    
    # traverse all collected items to check if folder to explore or file to log
    for filepath in filepaths:
        # if item is a sub-folder then explore recursively the resulting structure
        if os.path.isdir(os.path.join(path,filepath)):
            filenames = collect_files(os.path.join(path,filepath), filenames)
        
        # if item is a file, log the filepath in the output list
        elif os.path.isfile(os.path.join(path,filepath)):
            filenames.append(os.path.join(path,filepath))
    
    # return the list of files found in the whole structure            
    return filenames


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    
    # Validation of input arguments
    if path =='':
        print('**** please enter a proper directory path ****')
        return []
    if suffix == '':
        print('**** please enter a proper file extension ****')
        return []
    
    # Initialize file search
    filenames = []
    
    # Call search function if path is a directory otherwise check the suffix
    if os.path.isdir(path):
        filenames = collect_files(path, filenames)
    elif os.path.isfile(path) and path.endswith(suffix):
        filenames.append(path)
    # defensive code in case the path is neither a dirpath or a filepath
    else:
        return []
    
    # Filter the targeted files from the file list returned by the search function
    output =  []
    for file in filenames:             # Complexity is O(k) with k = total number of files found)
        if file.endswith(suffix):
            output.append(file)
    
    # return the list of files with targeted suffix
    return output






print('\n================= test 1 =====================')
suffix = '.c'
path = 'testdir'
if len(find_files(suffix, path))>0:
    
    print('found {} files with extention "{}" in directory "{}" :'.format(len(find_files(suffix, path)),
                                                                      suffix, path))
    for file in find_files(suffix, path):
        print(file)
else:
    print('No files found')

assert (find_files(suffix, path) == ['testdir\\subdir1\\a.c', 'testdir\\subdir3\\subsubdir1\\b.c', 'testdir\\subdir5\\a.c', 'testdir\\t1.c'])


# test cases
print('\n================= test 2 =====================')
suffix = ''
path = 'testdir'
if len(find_files(suffix, path))>0:
    
    print('found {} files with extention "{}" in directory "{}" :'.format(len(find_files(suffix, path)),
                                                                      suffix, path))
    for file in find_files(suffix, path):
        print(file)
else:
    print('No files found')

       
print('\n================= test 3 =====================')
suffix = '.c'
path = ''
if len(find_files(suffix, path))>0:
    
    print('found {} files with extention "{}" in directory "{}" :'.format(len(find_files(suffix, path)),
                                                                      suffix, path))
    for file in find_files(suffix, path):
        print(file)
else:
    print('No files found')


print('\n================= test 4 =====================')
suffix = '.c'
path = 'testdirNone'
if len(find_files(suffix, path))>0:
    
    print('found {} files with extention "{}" in directory "{}" :'.format(len(find_files(suffix, path)),
                                                                      suffix, path))
    for file in find_files(suffix, path):
        print(file)
else:
    print('No files found')
    
    
print("\nAll tests passed!")